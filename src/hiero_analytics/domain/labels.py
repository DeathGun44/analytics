"""
This class defines logical groupings of GitHub labels that represent
analytics concepts such as onboarding issues, difficulty levels, and
issue classifications.

Analytics code can therefore operate on `LabelSpec` objects instead of
hard coded raw strings, which improves maintainability and consistency.

Example
-------
Instead of writing:

    if "good first issue" in issue_labels:
        ...

analytics code should use the domain model:

    if GOOD_FIRST_ISSUE.matches(issue_labels):
        ...

"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, FrozenSet


@dataclass(frozen=True)
class LabelSpec:
    """
    A `LabelSpec` groups one or more raw GitHub labels under a single
    conceptual name (for example "Good First Issue" or "Bug").

    This abstraction allows analytics code to reason about label
    concepts without depending on the exact label strings used
    in the repository.

    Attributes
    ----------
    name : str
        Human-readable name for the label group.
    labels : frozenset[str]
        GitHub label strings belonging to this group.

    Typical usage
    -------------
    Matching issue labels:

        if GOOD_FIRST_ISSUE.matches(issue_labels):
            ...

    Iterating across difficulty levels:

        for level in DIFFICULTY_LEVELS:
            if level.matches(issue_labels):
                difficulty = level.name
                break
    """

    name: str
    labels: FrozenSet[str]

    def matches(self, issue_labels: Iterable[str] | None) -> bool:
        """
        Return True if any of the issue labels belong to this label group.

        Parameters
        ----------
        issue_labels : Iterable[str] | None
            Labels attached to a GitHub issue.

        Returns
        -------
        bool
            True if the issue contains any label from this group.
        """
        if not issue_labels:
            return False

        normalized = {label.lower() for label in issue_labels}
        return bool(self.labels.intersection(normalized))

    def __contains__(self, issue_labels: Iterable[str]) -> bool:
        """
        Allow membership-style checks.

        Example
        -------
        if issue_labels in GOOD_FIRST_ISSUE:
            ...
        """
        return self.matches(issue_labels)

    def __or__(self, other: "LabelSpec") -> "LabelSpec":
        """
        Combine two label groups into a new label specification.

        Example
        -------
        ALL_ONBOARDING = GOOD_FIRST_ISSUE | GOOD_FIRST_ISSUE_CANDIDATE
        """
        return LabelSpec(
            name=f"{self.name} + {other.name}",
            labels=self.labels | other.labels,
        )


# ------------------------------------------------------------------
# Onboarding labels
# ------------------------------------------------------------------

GOOD_FIRST_ISSUE = LabelSpec(
    name="Good First Issue",
    labels=frozenset(
        {
            "good first issue",
            "skill: good first issue",
        }
    ),
)

GOOD_FIRST_ISSUE_CANDIDATE = LabelSpec(
    name="Good First Issue Candidate",
    labels=frozenset(
        {
            "good first issue candidate",
        }
    ),
)

# Uses the `__or__` operator defined in `LabelSpec` to combine the two onboarding groups
ALL_ONBOARDING = GOOD_FIRST_ISSUE | GOOD_FIRST_ISSUE_CANDIDATE