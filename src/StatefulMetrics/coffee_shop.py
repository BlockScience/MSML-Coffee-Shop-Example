from Types import NumberConsumersType

coffee_shop_stateful_metrics = {"name": "Coffee Shop Stateful Metrics",
                                "notes": None,
                                "metrics": [{"type": NumberConsumersType,
                                             "name": "queue_length",
                                             "description": "len(state['queue'])",
                                             "variables_used": ["queue"],
                                             "parameters_used": [],
                                             "symbol": None,
                                             "domain": None}]}
