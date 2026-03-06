"""
This module provides functions to search for issues on GitHub using the REST API. 
It supports pagination to handle large result sets and allows for complex search queries using GitHub's search syntax.
"""
from __future__ import annotations

from typing import List, Dict, Any

from .github_client import GitHubClient
from .pagination import paginate_page_number


def search_issues(
    client: GitHubClient,
    query: str,
) -> List[Dict[str, Any]]:

    def page(p: int):

        url = (
            f"https://api.github.com/search/issues"
            f"?q={query}&per_page=100&page={p}"
        )

        data = client.get(url)

        return data.get("items", [])

    return paginate_page_number(page)