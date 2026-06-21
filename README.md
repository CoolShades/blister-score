# BLISTER Score

A compact, single-screen, installable (PWA) clinical calculator for the
**BLISTER score** — predicting cardiac implantable electronic device (CIED)
infection risk and deciding whether a **TYRX antimicrobial envelope** is
warranted. Built for **West Suffolk NHS Foundation Trust · Cardiology** in the
*Glacier* blue palette. Designed to fit one screen with minimal scrolling.

## What it does

- A slim sticky header; the seven BLISTER domains laid out as an **acronym
  spine** — the letters **B**lood results, **L**ong procedure, **I**mmunosuppressed,
  **S**ixty-or-younger, **T**ype of procedure, **E**arly reintervention,
  **R**epeat procedure run down the left and light up as each domain scores —
  each with its criteria as inline chips; and a **sticky result panel** that
  stays in view as you toggle, so the answer is always visible without scrolling.
- Live total score; **score ≥ 6 → antimicrobial envelope warranted**, with the
  modelled outcomes: ~30 % relative reduction in CIED infection, number needed
  to treat = 31, and £18,446 per QALY (within NICE thresholds).
- A copyable clerk note (collapsible in the result panel).
- About / source / disclaimer / version + changelog in a modal off the header.
- Full WSH branding.

No patient data is stored or transmitted — everything runs in the browser.

## Running it

It is a static site. Open `index.html` directly to use the calculator, but to
get **app install + offline support** it must be served over `http(s)` or
`localhost` (service workers and the install prompt don't run from `file://`):

```sh
cd blister-score
python -m http.server 8000
# then open http://localhost:8000
```

Deploy by copying the folder to any static host (GitHub Pages, NHS intranet
web server, etc.). For installability the host must serve it over HTTPS.

## Installing as an app

- **Android / Chrome / Edge:** an "Install BLISTER Score" card appears, or use
  the browser menu → *Install app*.
- **iOS / Safari:** tap **Share → Add to Home Screen** (the card shows this).

## Source

Maclean E, Mahtani K, Honarbakhsh S, et al. *BLISTER Score: A Novel, Externally
Validated Tool for Predicting Cardiac Implantable Electronic Device Infections,
and Its Cost-Utility Implications for Antimicrobial Envelope Use.* Circ Arrhythm
Electrophysiol. 2024;17:e012446. DOI: 10.1161/CIRCEP.123.012446.

Clinical decision support only — not a substitute for clinical judgement or
local infection-prevention policy.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The entire app (markup, styles, logic) |
| `manifest.webmanifest` | PWA manifest |
| `sw.js` | Service worker (offline cache) |
| `favicon.svg` | Tab icon (blood-drop) + `.ico`/`-32.png` fallbacks |
| `icon-192/512.png`, `icon-maskable-512.png`, `apple-touch-icon.png` | App / home-screen icons (shield + ECG) |
| `make_icons.py` | Regenerates the shield app icons |

## Version

**v1.0.0** — June 2026. See the in-app *Changelog* section.
