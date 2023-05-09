from Types import DeltaTimeType

system_stateful_metrics = {"name": "System Stateful Metrics",
                           "notes": None,
                           "metrics": [{"type": DeltaTimeType,
                                        "name": "time_passed",
                                        "description": "state['current_time'] - params['start_time']",
                                        "variables_used": ["current_time"],
                                        "parameters_used": ["start_time"],
                                        "symbol": None,
                                        "domain": None}]}
