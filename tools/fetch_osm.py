"""Fetch each course's OpenStreetMap outline, hole lines and greens into osm/<course>.json.

Runs on GitHub Actions (.github/workflows/osm.yml) so the phone can load the map data from the
Pocket Caddie site instead of waiting on the busy public Overpass servers.
Data (c) OpenStreetMap contributors, ODbL (https://www.openstreetmap.org/copyright).
"""
import json, re, sys, time, urllib.parse, urllib.request

SERVERS = ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter",
           "https://overpass.private.coffee/api/interpreter"]
# Same names and starting points as index.html (COURSE_PT); the name search box is wide, so they can be rough.
COURSES = {"rancho": ("Rancho Park", 34.0447, -118.4145), "westchester": ("Westchester", 33.9563, -118.4182)}


def ask(q):
    last = ""
    for _round in range(3):
        for u in SERVERS:
            try:
                req = urllib.request.Request(u, data=("data=" + urllib.parse.quote(q)).encode(),
                                             headers={"User-Agent": "pocket-caddie-map-fetch (github actions)"})
                with urllib.request.urlopen(req, timeout=120) as r:
                    return json.load(r)["elements"]
            except Exception as e:  # busy server: try the next one
                last = f"{u}: {e}"
                print("  retry:", last, file=sys.stderr)
        time.sleep(30)
    raise RuntimeError(last)


def rings(e):
    pts = lambda g: [(p["lat"], p["lon"]) for p in g or []]
    if e["type"] == "relation":
        return [pts(m.get("geometry")) for m in e.get("members", []) if m.get("role") != "inner" and m.get("geometry")]
    return [pts(e.get("geometry"))]


ok = True
for cid, (name, lat, lon) in COURSES.items():
    print("Course:", cid)
    try:
        b = f"{lat - 0.12},{lon - 0.15},{lat + 0.12},{lon + 0.15}"
        q1 = (f'[out:json][timeout:60];(way["leisure"="golf_course"]["name"~"{name}",i]({b});'
              f'relation["leisure"="golf_course"]["name"~"{name}",i]({b}););out geom;')
        found = ask(q1)
        def box(e):
            pts = [p for r in rings(e) for p in r]
            if not pts:
                return None
            return min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts)
        cands = [(e.get("tags", {}).get("name", ""), box(e)) for e in found]
        cands = [c for c in cands if c[1]]
        main = [c for c in cands if not re.search(r"par[ -]?3|3[ -]?par|nine|9[ -]hole|executive|pitch", c[0], re.I)] or cands
        if main:
            bx = max(main, key=lambda c: (c[1][2] - c[1][0]) * (c[1][3] - c[1][1]))[1]
            lat, lon = (bx[0] + bx[2]) / 2, (bx[1] + bx[3]) / 2
        R = 1300 if main else 2500
        q2 = (f'[out:json][timeout:60];(way["golf"="hole"](around:{R},{lat},{lon});'
              f'way["golf"="green"](around:{R},{lat},{lon}););out geom tags;')
        near = ask(q2)
        out = {"at": time.strftime("%Y-%m-%d"), "center": {"lat": round(lat, 6), "lon": round(lon, 6)},
               "course": found, "near": near,
               "attribution": "Data (c) OpenStreetMap contributors, ODbL"}
        with open(f"osm/{cid}.json", "w") as f:
            json.dump(out, f, separators=(",", ":"))
        print(f"  {len(found)} course outlines, {sum(1 for e in near if e.get('tags', {}).get('golf') == 'hole')} hole lines, "
              f"{sum(1 for e in near if e.get('tags', {}).get('golf') == 'green')} greens")
    except Exception as e:
        ok = False
        print("  failed:", e, file=sys.stderr)
sys.exit(0 if ok else 1)
