"""
Run Python SDK difficulty analysis.

Produces:
- Issue difficulty distribution pie
- Closed issue difficulty distribution pie
"""

from __future__ import annotations

from hiero_analytics.data_sources.github_client import GitHubClient
from hiero_analytics.data_sources.github_ingest import fetch_repo_issues_graphql

from hiero_analytics.transform.dataframe import issues_to_dataframe
from hiero_analytics.transform.save import save_dataframe

from hiero_analytics.metrics.difficulty import difficulty_distribution

from hiero_analytics.metrics.plotting.pie import plot_pie
from hiero_analytics.config.paths import ensure_output_dirs, DATA_DIR, CHARTS_DIR
from hiero_analytics.config.paths import ORG, REPO

def main() -> None:

    ensure_output_dirs()

    print(f"Running difficulty analysis for {ORG}/{REPO}")

    client = GitHubClient()

    issues = fetch_repo_issues_graphql(
        client,
        owner=ORG,
        repo=REPO,
    )

    print("Total issues:", len(issues))

    df = issues_to_dataframe(issues)

    issue_difficulty = difficulty_distribution(df)

    save_dataframe(
        issue_difficulty,
        DATA_DIR / "python_sdk_issue_difficulty.csv",
    )

    closed_df = df[df["state"] == "closed"]

    closed_difficulty = difficulty_distribution(closed_df)

    save_dataframe(
        closed_difficulty,
        DATA_DIR / "python_sdk_closed_issue_difficulty.csv",
    )

    plot_pie(
        issue_difficulty,
        label_col="difficulty",
        value_col="count",
        title="Python SDK Issue Difficulty Distribution",
        output_path=CHARTS_DIR / "python_sdk_issue_difficulty_pie.png",
    )

    plot_pie(
        closed_difficulty,
        label_col="difficulty",
        value_col="count",
        title="Python SDK Closed Issue Difficulty Distribution",
        output_path=CHARTS_DIR / "python_sdk_closed_issue_difficulty_pie.png",
    )

    print("Charts generated")


if __name__ == "__main__":
    main()