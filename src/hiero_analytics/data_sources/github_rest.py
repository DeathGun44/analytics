"""
This module provides functions to fetch data from the GitHub REST API, including repositories and issues for a given organization.
It uses pagination to handle large datasets and supports filtering issues by label.
"""
from __future__ import annotations

from typing import List, Dict, Any

from .github_client import GitHubClient
from .pagination import paginate_page_number


def fetch_org_repos(
    client: GitHubClient,
    org: str,
) -> List[str]:

    def page(p: int):

        url = f"https://api.github.com/orgs/{org}/repos?per_page=100&page={p}"

        data = client.get(url)

        return [
            repo["full_name"]
            for repo in data
            if isinstance(repo, dict) and "full_name" in repo
        ]

    return paginate_page_number(page)


def fetch_repo_issues(
    client: GitHubClient,
    repo: str,
    label: str | None = None,
) -> List[Dict[str, Any]]:

    def page(p: int):

        base_url = (
            f"https://api.github.com/repos/{repo}/issues"
            f"?state=all&per_page=100&page={p}"
        )

        if label:
            base_url += f"&labels={label}"

        data = client.get(base_url)

        return [
            issue
            for issue in data
            if isinstance(issue, dict)
        ]

    return paginate_page_number(page)