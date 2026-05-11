"""Atomic memory writes + git auto-commit.

Routines call these helpers to persist state. Auto-commit is critical because cloud
routines clone fresh — if changes aren't pushed to main, the next routine sees nothing.
"""
from __future__ import annotations

import datetime as dt
import subprocess
from pathlib import Path

MEMORY_DIR = Path(__file__).resolve().parents[2] / "memory"
REPO_ROOT = Path(__file__).resolve().parents[2]


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


def overwrite(filename: str, content: str) -> Path:
    """Overwrite a file in memory/ atomically. Use for state files (portfolio.md)."""
    path = MEMORY_DIR / filename
    _atomic_write(path, content)
    return path


def append(filename: str, content: str) -> Path:
    """Append to a file in memory/ (creates if missing). Use for logs."""
    path = MEMORY_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(content)
        if not content.endswith("\n"):
            f.write("\n")
    return path


def daily_snapshot(content: str, *, date: dt.date | None = None) -> Path:
    """Append to memory/daily/YYYY-MM-DD.md."""
    date = date or dt.date.today()
    path = MEMORY_DIR / "daily" / f"{date.isoformat()}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(content)
        if not content.endswith("\n"):
            f.write("\n")
    return path


def git_commit_and_push(message: str) -> tuple[bool, str]:
    """Stage memory/, commit, and push to origin main.

    Returns (success, output). If nothing to commit, returns (True, "nothing to commit").
    Designed to be safe to call inside Claude Code routines — failures don't raise so
    the routine can still log and notify.
    """
    try:
        # Stage only the memory/ dir — never touch src/ or routine prompts here.
        subprocess.run(
            ["git", "add", "memory/"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        # Check if there's anything staged
        status = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=REPO_ROOT,
            capture_output=True,
        )
        if status.returncode == 0:
            return True, "nothing to commit"

        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        push = subprocess.run(
            ["git", "push", "origin", "HEAD:main"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return True, push.stdout + push.stderr
    except subprocess.CalledProcessError as e:
        return False, f"git error: {e.stderr or e.stdout or e}"


def routine_commit(routine_slug: str) -> tuple[bool, str]:
    """Standard commit message format for routine memory updates."""
    now = dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    return git_commit_and_push(f"routine: {routine_slug} @ {now}")
