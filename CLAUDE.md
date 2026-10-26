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
- Laser rangefinder: Revasri. Its readings go in Pocket Caddie's "type the yardage" box.
- Golf balls on hand (not yet chosen): Callaway Supersoft, PXG Xtreme Tour X, Trust Bison Soft (urethane cover).

## First launch-monitor numbers (from the golfer, 2026-10-26; patio net, Callaway Supersoft)
Not yet known whether these are single shots or averages. Lofts for both clubs not yet given.

| Club | Club mph | Smash | Carry / total yd | Launch angle | Launch dir | Apex ft | Shot type |
|---|---|---|---|---|---|---|---|
| 7-iron | 71 | 1.35 | 128 / 132 | 23.5° | 8.4 (right) | 73 | right |
| PW | 66 | 1.24 | 102 / 107 | 27.6° | 6.5 (right) | 61 | miss right |

Open items: confirm monitor alignment (both clubs start right), then 10-shot sessions; lofts; carries for other clubs.

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
