"""
A fake motor bus! so we can do some testing without having to connect to the real hardware.
"""

import enum
from typing import Any
import numpy as np

from lerobot.common.robot_devices.motors.utils import MotorsBus


class FakeTorqueMode(enum.Enum):
    ENABLED = 1
    DISABLED = 0


class FakeMotorsBus(MotorsBus):
    def __init__(self):
        pass

    def connect(self):
        pass

    def write(
        self,
        data_name,
        values: int | float | np.ndarray,
        motor_names: str | list[str] | None = None,
    ) -> None:
        pass

    def set_calibration(self, calibration: dict[str, Any]):
        pass

    def read(
        self, data_name: str, motor_names: str | list[str] | None = None
    ) -> np.ndarray:
        return np.zeros(0)

    def disconnect(self):
        print("Disconnecting fake motors bus")
        pass
