# Agentic Portfolio Site

Status: implemented locally.

## Goal

Build responsive public portfolio proof page for Agentic Developer positioning.

## What is built

- Static responsive portfolio page: `src/index.html`
- Visual system: `src/styles.css`
- Local server script: `scripts/serve.py`
- Structural verification script: `scripts/check_site.py`
- Desktop screenshot: `screenshots/desktop.png`
- Mobile screenshot: `screenshots/mobile.png`

## Run locally

```bash
cd /Users/nguyenduykhang/ai-automation-portfolio/projects/01-agentic-portfolio-site
python3 scripts/serve.py
```

Open:

```txt
http://127.0.0.1:4173/
```

## Verify

```bash
python3 scripts/check_site.py
```

Expected:

```txt
PASS
```

## Evidence

- Screenshots: `screenshots/desktop.png`, `screenshots/mobile.png`
- Test output: `runs/test_output.txt`
- Metrics: `metrics/build_metrics.json`
- Agent workflow: `ai_agents/workflow.md`

## Claim boundary

This is local static proof, not a deployed live website yet.
