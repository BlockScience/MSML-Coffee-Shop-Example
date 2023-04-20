from typing import NewType
from datetime import datetime, timedelta


USDType = NewType('USD', float)
TimeType = NewType("Time", datetime)
ConsumersServedType = NewType("Consumers Served", int)
NumberBaristasType = NewType("Number of Baristas", int)
ConsumerIDType = NewType("Consumer ID", int)
NumberConsumersType = NewType("Number of Consumers", int)
DeltaTimeType = NewType("Delta Time", timedelta)
