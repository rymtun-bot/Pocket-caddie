# Pocket Caddie notes

This repo is PUBLIC. Keep only golf equipment and page code here: no financial, health or personal details.

## How to help
- Use only numbers the user has given; ask when something is missing. Cite outside sources (URL + date accessed).
- Club suggestions use the user's own carry distances, adjusted for conditions they report.
- `index.html` is the on-course page, served at https://rymtun-bot.github.io/Pocket-caddie/ (GitHub Pages, main branch).
  It stores clubs, saved greens and shots in the phone's browser only.

## User's equipment (from their photos, 2026-10-25)
- Launch monitor: Rapsodo Mobile Launch Monitor, original model (label: Model No. MLM1.1). Reports carry, total, club speed,
  ball speed, launch angle, launch direction, smash factor, shot type, and apex in feet (an estimate: the unit measures
  no spin). Leave spin columns blank. Patio-net carry is also an estimate (ball flies ~8 ft into the net).
  Setup (Rapsodo FAQ, accessed 2026-10-26): monitor 6-8 ft behind the ball on the target line; ball ~8 ft from the net.
- PRGR Black Pocket HS-130A: bought 2026-10-28, being returned (golfer's decision 2026-10-31). The Rapsodo is the only
  launch monitor: use it for carry, launch, direction, and club/ball speed (speed progress = 10 real shots every 2 weeks).
  PRGR sessions stay in `practice/` for the record; its club speed was erratic and its carry estimates unreliable.
- Irons (from the golfer, 2026-10-26): TaylorMade RSi 2, standard set, TaylorMade TM7-215 graphite shaft, regular flex.
  Stock lofts per 2nd Swing's spec table (https://www.2ndswing.com/golf-clubs/iron-sets/taylormade-rsi-2-iron-set,
  accessed 2026-10-26; not a TaylorMade sheet): 7-iron 31°, 8-iron 35°, 9-iron 40°, PW 45°. The golfer's own lofts
  may differ if the clubs were ever bent; have them checked if gapping looks off.
- Wedges (from the golfer, 2026-10-31): gap wedge 50°, Lazarus; sand wedge 54°, Lazarus (Rapsodo labels it SW).
  Long clubs also in the bag: 1U, 2U, 3U (20°), 4U, 5U (26°, older King Cobra Baffler), 5W, 3W, driver.
- Driver (golfer's photos, 2026-11-01): TaylorMade SIM Max 10.5°, sleeve at STD LOFT, Fujikura Ventus 6-R shaft.
  SIM Max sleeve adjusts loft about ±2°, and adding loft opens the face (retailer and tuning-guide pages, accessed 2026-11-01).
- Fairway woods (golfer's photos, 2026-11-01): Cleveland Launcher XL Halo 3-wood 15° (Cleveland shaft, flex not shown);
  TaylorMade Burner 3-wood (sole appears to read 15°) and Burner 5-wood 18°, both TaylorMade REAX 49 R shafts.
  The "3W" in Rapsodo sessions so far is the Burner (golfer, 2026-11-01); the Cleveland 3W is untested.
  4U = Lazarus 21° (golfer, 2026-11-01). Adams Tight Lies 19° also in the photo: no data yet; role in the bag unconfirmed.
- Laser rangefinder: Revasri. Its readings go in Pocket Caddie's "type the yardage" box.
- Golf balls on hand (not yet chosen): Callaway Supersoft, PXG Xtreme Tour X, Trust Bison Soft (urethane cover).

## First launch-monitor numbers (from the golfer, 2026-10-26; patio net, Callaway Supersoft)
Hit from the golfer's usual setup (about 2-3 quarters under the toe at address), not the hip-hinge setup
(about 5 quarters on a rug) tried 2026-10-26. Not yet known whether these are single shots or averages. Stock lofts: 7-iron 31°, PW 45° (see equipment above).

| Club | Club mph | Smash | Carry / total yd | Launch angle | Launch dir | Apex ft | Shot type |
|---|---|---|---|---|---|---|---|
| 7-iron | 71 | 1.35 | 128 / 132 | 23.5° | 8.4 (right) | 73 | right |
| PW | 66 | 1.24 | 102 / 107 | 27.6° | 6.5 (right) | 61 | miss right |

Open items: confirm monitor alignment (both clubs start right), then 10-shot sessions; carries for other clubs. Launch gap 7-iron vs PW is only 4.1° for 14° of loft;
check on video whether the 7-iron is getting extra loft at impact.

## Practice sessions
One file per session in `practice/` (date, monitor, place, ball), with raw shots and a summary.
From Rapsodo screenshots, use only the top-line average row for each club; ignore the individual shot rows (golfer's
instruction, 2026-10-31). The golfer sends each club's averages separately.
- 2026-07-05 and 2026-09-02: Rapsodo driver averages at the Westchester range (`practice/2026-range-driver-history.md`).
- 2026-09-02: Rapsodo 8-iron, 9-iron, PW averages at the Westchester range (`practice/2026-09-02-rapsodo-range.md`).
- 2026-10-28: PRGR, patio, Supersoft, PW through 3W (`practice/2026-10-28-prgr-patio.md`).
- 2026-10-30: Rapsodo, patio, 9-iron averages (`practice/2026-10-30-rapsodo-patio.md`).
- 2026-10-31: Rapsodo + PRGR, patio, Supersoft, PW (`practice/2026-10-31-rapsodo-patio.md`).
- Current two-week plan and pre-shot routine: `practice/plan-2026-11.md` (first real round planned Tuesday 2026-12-01).
- Day-by-day session list to Dec 1: `practice/daily-sessions.md`.
- Home course game (hole-by-hole Westchester/Rancho on the patio): `practice/home-course-game.md`.
- `home.html` (Home Course page, linked from Setup) runs that game: Rapsodo carry/total/start direction place the ball;
  long first putts count as a lag; assumptions (green radius, fairway width, trouble, lag leaves) are editable on the page.
- Club list loading: one-tap link `https://rymtun-bot.github.io/Pocket-caddie/#clubs=Driver:185,8i:113` or paste
  "Driver 185, 8i 113" on the Clubs tab. Same-name clubs are updated, new ones added, nothing removed. Send both forms:
  on iPhone a Home Screen web app keeps its own storage, so the link (opens Safari) may not reach it; the paste box does.
- Competition mode (Setup tab): distance only for club/league events (Rule 4.3). Hides conditions, plays-like,
  club suggestion, club averages and green notes; keeps GPS yardages, the rangefinder box and shot measuring.

## Weather adjustments (added 2026-10-25, user chose "learn from my rounds")
- Live wind/temp/pressure from Open-Meteo at the phone's position; wind resolved along the line to the saved green.
- Plays-like = distance + wind + temperature + air-pressure terms + the user's own adjustment. Factors start at published
  averages (cited on the page's Setup tab) and are editable there.
- Each hole has free-text green notes (the user's own reads); "Copy all notes for this course" exports them.
- Every measured shot logs temp, pressure, wind, head/cross component along the actual shot line, and fairway/green
  firmness. When the user pastes a shot log, fit their own factors from it and tell them what to enter in Setup.
  Note: measured shot yards are total distance (carry + roll), so weigh firmness when fitting.

## Course data
- The golfer plays the Blue tees (Pocket Caddie default; changeable in Setup).
- Westchester scorecard (from the golfer, 2026-10-25) is built into index.html (CARDS) and in courses/westchester.md.
- Rancho Park scorecard (Greenskeeper.org screenshot from the golfer, 2026-10-25) is in CARDS and courses/rancho_park.md.
  Tees there: Black 6,839 / Blue 6,419 / White 6,036 / Yellow 5,644. Ask which tees the golfer plays at Rancho.
