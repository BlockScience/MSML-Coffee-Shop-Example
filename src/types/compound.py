from typing import NewType
from .primitives import TimeType, NumberBaristasType
from typing import Dict

BaristaScheduleType = NewType(
    'Barista Schedule', Dict[TimeType, NumberBaristasType])
