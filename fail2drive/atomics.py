"""Fail2Drive-specific atomic behaviors.

Carries the additions Fail2Drive made to srunner's
``scenariomanager.scenarioatomics.atomic_behaviors`` module.

ogbench-carla (and other consumers using a different srunner fork) inject
these symbols back into srunner's atomic_behaviors namespace at runtime so
Fail2Drive's scenario files can import them unmodified.

The class is copied verbatim from
``scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py``
in the Fail2Drive repo.
"""

from __future__ import print_function

import carla
import py_trees

from srunner.scenariomanager.carla_data_provider import CarlaDataProvider
from srunner.scenariomanager.scenarioatomics.atomic_behaviors import AtomicBehavior
from srunner.scenariomanager.timer import GameTime


__all__ = ["DeactivateBrakeLights"]


class DeactivateBrakeLights(AtomicBehavior):

    def __init__(self, duration, name="Idle"):
        """
        Setup actor
        """
        super(DeactivateBrakeLights, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))
        self._duration = duration

    def initialise(self):

        super(DeactivateBrakeLights, self).initialise()
        self._start_time = GameTime.get_time()

    def update(self):

        cars = CarlaDataProvider.get_all_actors().filter("vehicle.*")

        for c in cars:
            try:
                c.set_light_state(carla.VehicleLightState(c.get_light_state() & ~carla.VehicleLightState.Brake))
            except:
                print(f"Failed to turn off brake light for actor id: {c.id}")

        if GameTime.get_time() - self._start_time > self._duration:
            return py_trees.common.Status.SUCCESS

        return py_trees.common.Status.RUNNING
