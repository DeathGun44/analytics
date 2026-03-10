"""
Domain model for issue difficulty levels.

This module defines the `DifficultyLevel` class, which represents a classification of issue difficulty based on GitHub labels. 
It also provides a function to classify an issue's difficulty level based on its labels.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .labels import GOOD_FIRST_ISSUE, LabelSpec


@dataclass(frozen=True)
class DifficultyLevel:
    """
    Represents a difficulty classification.

    Attributes
    ----------
    name : str
        Human-readable name for the difficulty level.
    label_spec : LabelSpec
        LabelSpec defining the GitHub labels associated with this difficulty level.
    order : int
        Numerical order for sorting difficulty levels (lower means easier).
    """

    name: str
    label_spec: LabelSpec
    order: int

# No need to define Good First Issue as we can reuse the existing `GOOD_FIRST_ISSUE` label group as a difficulty level

BEGINNER = DifficultyLevel(
    name="Beginner",
    label_spec=LabelSpec("Beginner", frozenset({"beginner"})),
    order=1,
)

INTERMEDIATE = DifficultyLevel(
    name="Intermediate",
    label_spec=LabelSpec("Intermediate", frozenset({"intermediate"})),
    order=2,
)

ADVANCED = DifficultyLevel(
    name="Advanced",
    label_spec=LabelSpec("Advanced", frozenset({"advanced"})),
    order=3,
)

GOOD_FIRST = DifficultyLevel(
    name="Good First Issue",
    label_spec=GOOD_FIRST_ISSUE,
    order=0,
)

# Difficulty levels ordered from easiest to hardest
DIFFICULTY_LEVELS = (
    GOOD_FIRST,
    BEGINNER,
    INTERMEDIATE,
    ADVANCED,
)


def classify_difficulty(issue_labels: Iterable[str] | None) -> str | None:
    """
    Determine difficulty level for an issue.

    Parameters
    ----------
    issue_labels : Iterable[str] | None
        Labels attached to a GitHub issue.  
        Can be None if the issue has no labels.
    
    Returns
    -------
    str | None
        Name of the difficulty level if a match is found, otherwise None.
    """

    for level in DIFFICULTY_LEVELS:
        if level.label_spec.matches(issue_labels):
            return level.name

    return None