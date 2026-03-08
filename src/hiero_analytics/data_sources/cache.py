"""
File-based caching for GitHub API responses.

Functions:
    load_cache(key): Return cached data if it exists.
    save_cache(key, data): Store JSON-serializable data in the cache.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
from typing import Any
from hiero_analytics.config.paths import CACHE_DIR, ensure_output_dirs

# Create the cache directory if it doesn't exist
ensure_output_dirs()

def _path(key: str) -> Path:
    """
    Convert a cache key (typically a GitHub API endpoint) into a filesystem-safe
    path for storing cached JSON responses.

    GitHub API endpoints often contain characters such as "/" or ":" that are not
    suitable for filenames. This function replaces those characters with
    underscores to produce a valid filename.

    Args:
        key: Cache identifier, usually a GitHub API endpoint or query string.

    Returns:
        Path: Location of the cache file where the JSON response will be stored.

    Example:
        key = "repos/hiero-ledger/analytics/issues?state=open"

        -> Path(".cache/github/repos_hiero-ledger_analytics_issues?state=open.json")

    Notes:
        This function is used internally by `load_cache` and `save_cache` to
        determine the file location for cached API responses.
    """
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", key)    
    return CACHE_DIR / f"{safe}.json"

def save_cache(key: str, data: Any) -> None:
    """
    Save data to the cache for a given key.

    The key usually represents a GitHub API endpoint. The data is written as JSON
    to the cache file associated with that key so it can be reused later by
    `load_cache`.

    Args:
        key: Cache identifier, typically an API endpoint or query string.
        data: Python object to cache. Must be JSON serializable.

    Returns:
        None
    """
    with open(_path(key), "w") as f:
        json.dump(data, f)

def load_cache(key: str) -> Any | None:
    """
    Return cached data for a given key if it exists.

    The cache key typically corresponds to a GitHub API endpoint. If a matching
    cache file is found, its JSON contents are loaded and returned as a Python
    object. If no cache file exists, the function returns None.

    Args:
        key: Cache identifier, usually a GitHub API endpoint or query string.

    Returns:
        The cached data as a Python object, or None if no cache entry exists.

    Example:
        key = "repos/hiero-ledger/analytics/issues?state=open"

    """
    p = _path(key)

    if p.exists():
        with open(p) as f:
            return json.load(f)

    return None


