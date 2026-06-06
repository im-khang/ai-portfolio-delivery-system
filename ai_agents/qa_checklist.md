# QA Checklist

## Public content

- [ ] Direction says practical solutions, not generic web tools.
- [ ] Project cards show clean project names and GitHub links.
- [ ] Public pages stay focused on project outcomes, not internal work notes.
- [ ] Contact links and project links are valid.

## Static site checks

- [ ] Root pages parse as HTML.
- [ ] `src/` mirrored pages parse as HTML.
- [ ] `python3 scripts/check_site.py` returns `PASS`.
- [ ] Vercel `/projects` route returns HTTP `200` after deploy.

## Human review

- [ ] Claims stay tied to visible evidence.
- [ ] No private local paths are exposed in public content.
- [ ] README explains AI agent + Open Design workflow clearly.
