# AI Agent Workflow

## Human need

Build Project 1: a responsive portfolio site that positions Khang for Agentic Developer / AI Workflow Builder roles, with visible claim boundaries and no fake case studies.

## Agent tasks

- Inspected scaffold and tool availability.
- Built static HTML/CSS page.
- Added local server script.
- Added structural verification script.
- Ran local server and generated desktop/mobile screenshots with headless Chrome.

## Human checks encoded

- Public copy avoids production claims without proof.
- Case section labels future projects as local plans, not completed work.
- Claim boundary table separates proven locally, blueprint-ready, and need-live-proof tools.
- Contact and GitHub/LinkedIn links included.

## Debug/fix log

- Previous tool turn returned empty response after initialization; continued by processing results and building site.
- Server process was started as long-lived background process and killed after screenshots.

## Verification

- `python3 scripts/check_site.py` returned `PASS`.
- Local HTTP fetch found `Agentic Developer` in HTML.
- Headless Chrome generated `screenshots/desktop.png` and `screenshots/mobile.png`.
