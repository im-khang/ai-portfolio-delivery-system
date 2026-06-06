#!/usr/bin/env python3
"""Sync accepted Open Design portfolio artifact into this static publish repo.

Source of truth:
  Open Design project 3f80c890-4515-4943-ac71-04b29a1954af

Publish target:
  this repository root and src/ mirror, used by Vercel rewrites.
"""
from __future__ import annotations

import shutil
from pathlib import Path

PROJECT_ID = "3f80c890-4515-4943-ac71-04b29a1954af"
OD_PROJECT_DIR = Path("/Users/nguyenduykhang/open-design/.od/projects") / PROJECT_ID
REPO_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_DIR / "src"

TEXT_FILES = ["index.html", "styles.css"]
BINARY_FILES = ["profile-image.jpg"]
MIRRORED_PAGES_TO_PATCH = [
    "index.html",
    "src/index.html",
    "about.html",
    "src/about.html",
    "projects.html",
    "src/projects.html",
]

COPY_REPLACEMENTS = {
    "Khang Nguyen builds small web tools and AI-assisted workflows with clear verification evidence.":
        "Khang Nguyen builds practical solutions and AI-assisted workflows with clear verification evidence.",
    "AI workflow builder focused on practical web tools, agent-assisted delivery, and honest proof.":
        "AI workflow builder focused on practical solutions, agent-assisted delivery, and honest proof.",
    "I build practical web tools with <span class=\"text-glow\">AI agents</span> and <span class=\"text-glow\">human review</span>.":
        "I build practical solutions with <span class=\"text-glow\">AI agents</span> and <span class=\"text-glow\">human review</span>.",
    "I build practical web tools with <span class=\"text-glow\">AI agents</span>, data tools, and human review.":
        "I build practical solutions with <span class=\"text-glow\">AI agents</span>, data tools, and human review.",
    "I turn unclear team needs into small, testable systems: pages, automations, dashboards, and application workflows.":
        "I turn unclear team needs into small, testable solutions: automations, dashboards, workflows, and decision support systems.",
    "My focus is small, testable systems: pages, automations, dashboards, and application workflows that can be checked with real evidence.":
        "My focus is small, testable solutions: automations, dashboards, workflows, and decision support systems that can be checked with real evidence.",
    "If you need a small web tool, workflow prototype, or AI-assisted build with real verification, send me the context and goal.":
        "If you need a practical solution, workflow prototype, or AI-assisted build with real verification, send me the context and goal.",
}


def copy_file(name: str) -> None:
    source = OD_PROJECT_DIR / name
    if not source.exists():
        raise FileNotFoundError(source)
    for target in (REPO_DIR / name, SRC_DIR / name):
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix.lower() in {".html", ".css", ".js", ".json", ".txt", ".md"}:
            target.write_text(source.read_text())
        else:
            shutil.copy2(source, target)
        print(f"synced {source} -> {target}")


def patch_copy(path: Path) -> None:
    if not path.exists():
        return
    text = path.read_text()
    new_text = text
    for old, new in COPY_REPLACEMENTS.items():
        new_text = new_text.replace(old, new)
    if new_text != text:
        path.write_text(new_text)
        print(f"patched copy {path}")


def main() -> None:
    if not OD_PROJECT_DIR.exists():
        raise SystemExit(f"Open Design project dir missing: {OD_PROJECT_DIR}")
    for name in TEXT_FILES + BINARY_FILES:
        copy_file(name)
    for rel in MIRRORED_PAGES_TO_PATCH:
        patch_copy(REPO_DIR / rel)


if __name__ == "__main__":
    main()
