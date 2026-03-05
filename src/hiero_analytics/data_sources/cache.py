"""
This module provides a simple caching mechanism for GitHub API responses. It saves responses to the local
filesystem in a .cache/github directory, using a sanitized version of the API endpoint as the filename. This can help speed up development and reduce API calls during testing.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CACHE_DIR = Path(".cache/github")
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def _path(key: str) -> Path:
    safe = key.replace("/", "_").replace(":", "_")
    return CACHE_DIR / f"{safe}.json"


def load_cache(key: str) -> Any | None:
    p = _path(key)

    if p.exists():
        with open(p) as f:
            return json.load(f)

    return None


def save_cache(key: str, data: Any) -> None:
    with open(_path(key), "w") as f:
        json.dump(data, f)