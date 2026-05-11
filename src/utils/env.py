"""Local .env loader for smoke tests.

Cloud routines set env vars directly in the Claude Cloud Environment — they don't have
a .env file. This helper is a no-op there but loads .env when running locally.
"""
from __future__ import annotations

from pathlib import Path


def load_local_env() -> None:
    """Load .env from repo root if present. Safe to call anywhere — no-op if missing."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return  # python-dotenv not installed: assume env is already set
    env_path = Path(__file__).resolve().parents[2] / ".env"
    if env_path.exists():
        load_dotenv(env_path, override=False)
