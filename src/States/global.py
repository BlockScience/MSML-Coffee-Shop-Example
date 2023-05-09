from .Types import Time

global_state = {"Name": "Global State",
                "notes": "The system-wide state",
                "variables": [{"type": Time,
                               "name": "Time",
                               "description": "System clock",
                               "symbol": "T",
                               "domain": "12AM-11: 59PM"}]}
