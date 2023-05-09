from Types import CurrencyType, BaristaScheduleType

coffee_shop_parameters = {"name": "Coffee Shop Parameters",
                          "notes": "Any parameters specific to the coffee shop",
                          "parameters": [{"variable_type": CurrencyType,
                                          "name": "employee_cost",
                                          "description": "The $ cost per employee per hour"},
                                         {"variable_type": BaristaScheduleType,
                                          "name": "barista_schedule",
                                          "description": "A schedule of the number of baristas on shift at each time"}
                                         ]}
