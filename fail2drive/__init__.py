"""Fail2Drive route + scenario discovery helpers.

* ``ROUTES_DIR`` points at the directory containing the 200 Fail2Drive route
  XML files (100 ``Base_*`` in-distribution routes and 100 ``Generalization_*``
  long-tail evaluation routes).
* ``SCENARIOS_DIR`` points at the directory containing byte-identical copies
  of the Fail2Drive scenario classes (the ``.py`` files vendored from
  ``scenario_runner/srunner/scenarios/``). Downstream consumers add this dir
  to their leaderboard's scenario discovery so the ``ImageOnObject``,
  ``ObscuredStopSign``, ``RoadBlocked``, etc. classes referenced by the route
  XMLs resolve.
* ``fail2drive.atomics`` carries the ``DeactivateBrakeLights`` atomic that
  Fail2Drive added to ``atomic_behaviors``; inject it into srunner's namespace
  before importing the scenario files.
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path

__all__ = ["ROUTES_DIR", "SCENARIOS_DIR"]


def _resolve_routes_dir() -> Path:
    return Path(str(resources.files("fail2drive_split"))).resolve()


def _resolve_scenarios_dir() -> Path:
    # The vendored scenario files live as data inside this package.
    return (Path(__file__).resolve().parent / "scenarios").resolve()


ROUTES_DIR: Path = _resolve_routes_dir()
SCENARIOS_DIR: Path = _resolve_scenarios_dir()
