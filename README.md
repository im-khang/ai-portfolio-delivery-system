# Agentic Portfolio Site

A responsive portfolio website built to showcase practical solutions, AI-assisted delivery, and human-reviewed project work.

Live site: https://01-agentic-portfolio-site.vercel.app/

## What this project demonstrates

- Turning a personal positioning brief into a shipped static portfolio.
- Using AI agents to draft, edit, QA, and iterate on site content.
- Using Open Design as the visual source workflow, then syncing accepted output into a deployable static repo.
- Keeping public copy concise, proof-backed, and recruiter-friendly.
- Verifying pages with automated checks before deploy.

## Pages

- `index.html` — hero, positioning, skills, process, and contact.
- `about.html` — background, working style, and AI/data focus.
- `projects.html` — clean project showcase with GitHub links.

## Featured project links

- Agentic Portfolio Site: https://github.com/im-khang/agentic-portfolio-site
- Sales Forecasting Decision Support: https://github.com/im-khang/Sales-Forecasting-Using-PyCaret
- Superstore Performance Analytics: https://github.com/im-khang/Superstore-Dashboard
- AdventureWorks BI Operations: https://github.com/im-khang/AdventureWorks-Dashboard

## Workflow

1. Define portfolio direction and claim boundaries.
2. Generate and refine the visual direction in Open Design.
3. Sync accepted static HTML/CSS into this repository.
4. Patch copy and links in source and mirrored public files.
5. Run structural checks and stale-copy checks.
6. Push to GitHub and deploy through Vercel.

## Verification

```bash
python3 scripts/check_site.py
```

Expected result:

```text
PASS
```

Additional checks used before deploy:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
for name in ['index.html','about.html','projects.html','src/index.html','src/about.html','src/projects.html']:
    HTMLParser().feed(Path(name).read_text())
    print('html_parse_ok', name)
PY
```

## Deployment

This repo is configured for Vercel static deployment with clean URLs via `vercel.json`.

Production URL:

```text
https://01-agentic-portfolio-site.vercel.app/
```

## Repository structure

```text
src/                 mirrored source pages and styles used by Vercel rewrites
scripts/             sync, local serve, and verification scripts
ai_agents/           public workflow notes for AI-assisted build process
screenshots/         desktop and mobile visual evidence
metrics/             lightweight build and QA metrics
```

## Claim boundary

This project demonstrates a shipped static portfolio workflow using AI agents, Open Design, human review, and verification. It does not claim production backend integrations or enterprise-scale automation.
