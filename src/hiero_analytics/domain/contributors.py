"""
Domain model for contributor roles.

Defines logical classifications of contributors used in analytics.
These roles are inferred from GitHub metadata such as author type,
commit history, or contribution counts.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ContributorRole:
    """
    Represents a type of contributor in the ecosystem.

    Attributes
    ----------
    name : str
        Human-readable role name.
    """

    name: str


# --------------------------------------------------
# Contributor role definitions
# --------------------------------------------------

CORE_MAINTAINER = ContributorRole("Core Maintainer")

FIRST_TIME_CONTRIBUTOR = ContributorRole("First Time Contributor")

BOT = ContributorRole("Bot")


CONTRIBUTOR_ROLES = (
    CORE_MAINTAINER,
    FIRST_TIME_CONTRIBUTOR,
    BOT,
)