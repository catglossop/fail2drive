"""Fail2Drive scenario classes (vendored from scenario_runner/srunner/scenarios).

The ``*.py`` files in this directory are byte-identical copies of the
corresponding files under ``scenario_runner/srunner/scenarios/`` in the
Fail2Drive repo. They are shipped here so downstream consumers (using a
different srunner fork) can register the Fail2Drive scenario classes with
their own leaderboard's discovery without vendoring the full
``scenario_runner`` tree.

See :data:`fail2drive.SCENARIOS_DIR` for the on-disk location.
"""
