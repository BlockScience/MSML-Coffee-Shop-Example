
from Types import ConsumerIDType, DeltaTimeType
consumer_state = {"name": "Consumer State",
                  "notes": "There will be 0+ of these states, based on queue length",
                  "variables": [{"type": ConsumerIDType,
                                 "name": "id",
                                 "description": "The id of the customer, must be unique",
                                 "symbol": None,
                                 "domain": None},
                                {"type": DeltaTimeType,
                                 "name": "time_waited",
                                 "description": "The time the customer has waited, init at 0",
                                 "symbol": None,
                                 "domain": None}]}
