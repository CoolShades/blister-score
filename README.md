# BLISTER Score

An installable (PWA) clinical calculator for the **BLISTER score** — predicting
cardiac implantable electronic device (CIED) infection risk and deciding whether
a **TYRX antimicrobial envelope** is warranted. Built for **West Suffolk NHS
Foundation Trust · Cardiology** in the *Glacier* blue palette.

No patient data is stored or transmitted — everything runs in the browser.

## What it does

**Launch screen.** On open, a short animated sequence plays: a pacemaker is
wrapped in the TYRX antimicrobial envelope and seated into the device pocket,
then a pulsing antimicrobial force field repels infection. A **Go to Calculator**
button lifts the curtain to reveal the app, with a muted rainbow flourish
cascading down the BLISTER spine (B → R) — which then replays as a gentle
attract loop on the calculator until you tick the first factor. On wide screens it's a split hero — the
animation beside a column carrying the wordmark, the key figures
(≥6 → fit envelope · ≈30 % fewer infections · NNT 31) and the calls to action;
on narrow screens it collapses to a centred card. An **About** button opens the
source, disclaimer and changelog.

**Calculator.** The seven BLISTER domains run down the left as an **acronym
spine** — **B**lood results, **L**ong procedure, **I**mmunosuppressed,
**S**ixty-or-younger, **T**ype of procedure, **E**arly reintervention,
**R**epeat procedure. Each letter lights up and shows a small score badge as its
domain contributes. Every factor is a checkbox sitting beneath its domain name:

- **Mutually-exclusive options are handled automatically** — ticking one age
  band, one device box-change type (PPM / ICD / CRT) or one previous-procedure
  count unticks its siblings.
- **Type of procedure can be combined** — a box change, a new / revised lead and
  a lead extraction can all be scored together (their points are additive).

A **result panel** shows the live total score and the verdict: **score ≥ 6 →
antimicrobial envelope warranted**, with two modelled outcomes (~30 % relative
reduction in CIED infection and an NNT of 31) shown once the threshold is
reached, and a "points to threshold" hint below it when you're short. It is a
sticky sidebar on desktop; on small screens the app becomes a shell — the
domains scroll between a fixed header and a static result panel docked above the
footer. **Copy note** puts a paste-ready pre-procedure summary on the clipboard
for the SOLUS record (score, factor breakdown and the envelope recommendation,
including the cost-utility figures and a prolonged-procedure caveat); **Reset**
clears all selections.

## Running it

It is a static site. Open `index.html` directly to use the calculator, but to
get **app install + offline support** it must be served over `http(s)` or
`localhost` (service workers and the install prompt don't run from `file://`):

```sh
cd blister-score
python -m http.server 8000
# then open http://localhost:8000
```

Deploy by copying the folder to any static host (GitHub Pages, NHS intranet web
server, etc.). For installability the host must serve it over HTTPS. The launch
animation plays on every load; the **Go to Calculator** button dismisses it.

## Installing as an app

- **Android / Chrome / Edge:** an "Install BLISTER Score" card appears, or use
  the browser menu → *Install app*.
- **iOS / Safari:** tap **Share → Add to Home Screen** (the card shows this).

## Source

Maclean E, Mahtani K, Honarbakhsh S, et al. *BLISTER Score: A Novel, Externally
Validated Tool for Predicting Cardiac Implantable Electronic Device Infections,
and Its Cost-Utility Implications for Antimicrobial Envelope Use.* Circ Arrhythm
Electrophysiol. 2024;17:e012446. DOI: 10.1161/CIRCEP.123.012446.

Clinical decision support only — not a substitute for clinical judgement or local
infection-prevention policy. The domain points and the ≥ 6 envelope threshold
follow the published model; combining procedure components (e.g. a box change
plus a lead extraction) sums their points, which extends the paper's
single-category treatment of procedure type.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The entire app — launch screen, calculator, styles and logic |
| `manifest.webmanifest` | PWA manifest |
| `sw.js` | Service worker (offline cache; bump `CACHE` to ship an update) |
| `favicon.svg` | Tab icon (blood-drop) + `.ico` / `-32.png` fallbacks |
| `icon-192/512.png`, `icon-maskable-512.png`, `apple-touch-icon.png` | App / home-screen icons (shield + ECG) |
| `make_icons.py` | Regenerates the shield app icons |

## Version

**v1.2.0** — June 2026. See the in-app *Changelog* (via **About**).
