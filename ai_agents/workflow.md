# AI Agent Workflow

## Human goal

Build and ship a concise portfolio website for Khang that communicates practical-solution work, AI-assisted delivery, and human-reviewed project judgment.

## Agent-assisted workflow

1. Interpret positioning constraints and public claim boundaries.
2. Generate and refine visual direction through Open Design.
3. Sync accepted static HTML/CSS into the repository.
4. Patch source and mirrored pages together so deployment output stays consistent.
5. Run automated page checks before push.
6. Verify deployed routes and GitHub links after push.

## Human review points

- Portfolio wording says “practical solutions,” not generic web tools.
- Project cards show clean names and GitHub links only.
- Public content does not expose internal rebuild notes or local audit process.
- Claims stay tied to visible evidence: repo, screenshots, command output, or live URL.
- Tone stays concise, recruiter-friendly, and honest.

## Verification used

- `python3 scripts/check_site.py`
- HTML parser checks for root and `src/` pages.
- Stale-copy search for outdated public wording.
- Live route check with `curl` after deployment.

## Result

The site was pushed to GitHub and deployed on Vercel with `/projects` returning HTTP `200` and expected GitHub links present.
