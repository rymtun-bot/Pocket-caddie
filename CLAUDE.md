# Pocket Caddie notes

This repo is PUBLIC. Keep only golf equipment and page code here: no financial, health or personal details.

## How to help
- Use only numbers the user has given; ask when something is missing. Cite outside sources (URL + date accessed).
- Club suggestions use the user's own carry distances, adjusted for conditions they report.
- `index.html` is the on-course page, served at https://rymtun-bot.github.io/Pocket-caddie/ (GitHub Pages, main branch).
  It stores clubs, saved greens and shots in the phone's browser only.

## User's equipment (from their photos, 2026-10-25)
- Launch monitor: Rapsodo Mobile Launch Monitor, original model (label: Model No. MLM1.1). Reports carry, club speed,
  ball speed, launch angle, launch direction, smash factor; no spin data, so leave spin/apex columns blank.
- Laser rangefinder: Revasri. Its readings go in Pocket Caddie's "type the yardage" box.
- Golf balls on hand (not yet chosen): Callaway Supersoft, PXG Xtreme Tour X, Trust Bison Soft (urethane cover).

## Weather adjustments (added 2026-10-25, user chose "learn from my rounds")
- Live wind/temp/pressure from Open-Meteo at the phone's position; wind resolved along the line to the saved green.
- Plays-like = distance + wind + temperature + air-pressure terms + the user's own adjustment. Factors start at published
  averages (cited on the page's Setup tab) and are editable there.
- Each hole has free-text green notes (the user's own reads); "Copy all notes for this course" exports them.
- Every measured shot logs temp, pressure, wind, head/cross component along the actual shot line, and fairway/green
  firmness. When the user pastes a shot log, fit their own factors from it and tell them what to enter in Setup.
  Note: measured shot yards are total distance (carry + roll), so weigh firmness when fitting.

## Course data
- Westchester scorecard (from the golfer, 2026-10-25) is built into index.html (CARDS) and in courses/westchester.md.
- Rancho Park: no scorecard from the golfer yet; do not add one from web sources.
