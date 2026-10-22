#!/usr/bin/env python3
"""Create a provenance-preserving *inventory*, not an automatically publishable curriculum.

Run after cloning the four forks into sources/<id>. No code or solutions are copied.
"""
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "curriculum/sources.json").read_text())
OUTPUT = ROOT / "curriculum/catalog.json"

def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")

def git_head(path):
    try:
        return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return None

def discover(source, base):
    kind = source["kind"]
    if kind == "exercism":
        config = base / "config.json"
        if not config.exists():
            raise ValueError("Exercism config.json missing")
        data = json.loads(config.read_text())
        for track in ("concept", "practice"):
            for item in data.get("exercises", {}).get(track, []):
                name = item["slug"]
                path = f"exercises/{track}/{name}"
                yield name, path, item.get("prerequisites", []), track
    elif kind == "days":
        for p in sorted(base.iterdir()):
            if p.is_dir() and re.match(r"(?i)^day[ _-]?[0-9]+", p.name):
                yield p.name, p.relative_to(base).as_posix(), [], "lesson"
    elif kind == "c1":
        for p in sorted((base / "curriculum").glob("week-*")):
            if p.is_dir():
                yield p.name, p.relative_to(base).as_posix(), [], "week"
    elif kind == "learn":
        # Generic discovery; human review required to identify actual project boundaries.
        for p in sorted(base.rglob("README.md")):
            if len(p.relative_to(base).parts) >= 2 and not any(x in p.parts for x in (".git", "node_modules", ".venv")):
                yield p.parent.name, p.parent.relative_to(base).as_posix(), [], "candidate"

def main():
    records = []
    for source in CONFIG["sources"]:
        base = ROOT / "sources" / source["id"]
        if not base.is_dir():
            print(f"SKIP {source['id']}: clone not found at {base}")
            continue
        sha = git_head(base)
        for name, path, prerequisites, kind in discover(source, base):
            records.append({
                "id": f"{source['id']}:{slug(path)}",
                "title": name.replace("-", " ").replace("_", " ").title(),
                "source": source["id"],
                "source_repo": source["repo"],
                "source_commit": sha,
                "source_path": path,
                "license": source["license"],
                "source_prerequisites": prerequisites,
                "type": kind,
                "status": "review_required",
                "evaluator_status": "not_verified",
                "learner_release": False,
            })
    ids = [r["id"] for r in records]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate challenge IDs")
    OUTPUT.write_text(json.dumps({"schema_version": 1, "items": records}, indent=2) + "\n")
    print(f"Wrote {len(records)} inventory entries to {OUTPUT}")

if __name__ == "__main__":
    main()
