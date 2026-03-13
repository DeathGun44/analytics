"""
Example script: search GitHub issues
"""

from hiero_analytics.config.logging import setup_logging
from hiero_analytics.data_sources.github_client import GitHubClient
from hiero_analytics.data_sources.github_search import search_issues

setup_logging()


def main() -> None:

    client = GitHubClient()

    query = "org:hiero-ledger is:issue label:bug state:open"
    results = search_issues(client, query)

    print(f"Query: {query}")
    print(f"Found {len(results)} matching issues\n")

    for issue in results[:5]:
        print(
            issue["html_url"],
            issue["number"],
            issue["title"],
        )


if __name__ == "__main__":
    main()

