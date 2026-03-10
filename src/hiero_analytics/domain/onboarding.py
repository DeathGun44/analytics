"""
Domain model for contributor onboarding stages.

Defines the logical stages that contributors typically move through
when entering an open-source project.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .labels import (
    LabelSpec,
    GOOD_FIRST_ISSUE,
)


@dataclass(frozen=True)
class OnboardingStage:
    """
    Represents a stage in the contributor onboarding pipeline.

    Attributes
    ----------
    name : str
        Human-readable stage name.
    label : LabelSpec | None
        Label group associated with this stage (if applicable).
    """

    name: str
    label: Optional[LabelSpec] = None


# --------------------------------------------------
# Label-driven onboarding stages
# --------------------------------------------------

GFI_STARTER = OnboardingStage(
    name="Good First Issue Starter",
    label=GOOD_FIRST_ISSUE,
)

# --------------------------------------------------
# Activity-driven stages (not label based)
# --------------------------------------------------

FIRST_PR = OnboardingStage(
    name="First Pull Request",
)

MERGED_FIRST_PR = OnboardingStage(
    name="Merged First Pull Request",
)


ONBOARDING_STAGES = (
    FIRST_PR,
    MERGED_FIRST_PR,
)