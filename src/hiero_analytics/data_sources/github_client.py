"""
Low-level GitHub HTTP client.

Handles authentication, connection reuse, rate limiting, and request execution
for both REST and GraphQL GitHub API calls.
"""

from __future__ import annotations

import time
from typing import Any

import requests

from hiero_analytics.config.github import (
    BASE_URL,
    HTTP_TIMEOUT_SECONDS,
    REQUEST_DELAY_SECONDS,
    github_headers,
)


class GitHubClient:
    """HTTP client for interacting with the GitHub API."""

    def __init__(self) -> None:
        """
        Initialize the client with a persistent HTTP session and
        authentication headers from configuration.
        """

        headers = github_headers()

        # Reusable session for connection pooling
        self.session = requests.Session()
        self.session.headers.update(headers)

    # --------------------------------------------------------
    # INTERNAL HELPERS
    # --------------------------------------------------------

    def _handle_rate_limit(self, response: requests.Response) -> None:
        """
        Check GitHub rate limit headers and sleep if necessary.

        GitHub provides:
            X-RateLimit-Remaining
            X-RateLimit-Reset
        """

        remaining = int(response.headers.get("X-RateLimit-Remaining", "1"))
        reset = int(response.headers.get("X-RateLimit-Reset", "0"))

        if remaining <= 0:
            wait_seconds = max(0, reset - int(time.time()))
            time.sleep(wait_seconds)

    def _request(self, method: str, url: str, **kwargs: Any) -> Any:
        """
        Execute an HTTP request with rate limiting and retry delay.

        Args:
            method: HTTP method ("GET", "POST", etc.)
            url: Target URL
            **kwargs: Additional parameters passed to requests

        Returns:
            Parsed JSON response
        """

        response = self.session.request(
            method,
            url,
            timeout=HTTP_TIMEOUT_SECONDS,
            **kwargs,
        )

        self._handle_rate_limit(response)

        # Small delay to avoid aggressive API usage
        time.sleep(REQUEST_DELAY_SECONDS)

        response.raise_for_status()

        return response.json()

    # --------------------------------------------------------
    # PUBLIC API METHODS
    # --------------------------------------------------------

    def get(self, url: str) -> Any:
        """
        Execute a GET request to a GitHub REST endpoint.

        Args:
            url: Full GitHub API URL

        Returns:
            Parsed JSON response
        """

        return self._request("GET", url)

    def graphql(self, query: str, variables: dict[str, Any]) -> Any:
        """
        Execute a GraphQL query against the GitHub API.

        Args:
            query: GraphQL query string
            variables: Variables passed to the query

        Returns:
            Parsed JSON response
        """

        payload = {
            "query": query,
            "variables": variables,
        }

        return self._request(
            "POST",
            f"{BASE_URL}/graphql",
            json=payload,
        )