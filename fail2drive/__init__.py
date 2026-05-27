"""Fail2Drive route discovery helpers.

``ROUTES_DIR`` points at the directory containing the 200 Fail2Drive route XML
files (100 ``Base_*`` in-distribution routes and 100 ``Generalization_*``
long-tail evaluation routes). Downstream consumers (e.g. ogbench-carla's
``route_registry``) resolve route lookups against this directory.
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path

__all__ = ["ROUTES_DIR"]


def _resolve_routes_dir() -> Path:
    # The XMLs are shipped as the ``fail2drive_split`` package (declared in
    # pyproject.toml so they're included in wheels). ``files()`` returns an
    # ``importlib.abc.Traversable``; convert to a concrete filesystem Path so
    # callers can pass it to anything that expects ``pathlib.Path``.
    return Path(str(resources.files("fail2drive_split"))).resolve()


ROUTES_DIR: Path = _resolve_routes_dir()
