"""
GitHubClient is a simple wrapper around the GitHub API that handles authentication and rate limiting.
"""
from __future__ import annotations

import os
import time
from typing import Any

import requests
from dotenv import load_dotenv

from hiero_analytics.config.github import (
    HTTP_TIMEOUT_SECONDS,
    REQUEST_DELAY_SECONDS,
)

load_dotenv()


class GitHubClient:

    BASE_URL = "https://api.github.com"

    def __init__(self) -> None:
        token = os.getenv("GITHUB_TOKEN")

        self.headers = {
            "Authorization": f"Bearer {token}"
        } if token else {}

    def get(self, url: str) -> Any:

        r = requests.get(
            url,
            headers=self.headers,
            timeout=HTTP_TIMEOUT_SECONDS,
        )

        remaining = int(r.headers.get("X-RateLimit-Remaining", "1"))
        reset = int(r.headers.get("X-RateLimit-Reset", "0"))

        if remaining <= 0:
            wait = max(0, reset - int(time.time()))
            time.sleep(wait)

            r = requests.get(
                url,
                headers=self.headers,
                timeout=HTTP_TIMEOUT_SECONDS,
            )

        time.sleep(REQUEST_DELAY_SECONDS)

        r.raise_for_status()
        return r.json()

    def graphql(self, query: str, variables: dict[str, Any]) -> Any:

        r = requests.post(
            f"{self.BASE_URL}/graphql",
            json={"query": query, "variables": variables},
            headers=self.headers,
            timeout=HTTP_TIMEOUT_SECONDS,
        )

        r.raise_for_status()

        return r.json()