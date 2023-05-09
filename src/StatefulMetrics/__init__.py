from .system import system_stateful_metrics
from .coffee_shop import coffee_shop_stateful_metrics
from .consumer import consumer_stateful_metrics


stateful_metrics = {"System": system_stateful_metrics,
                    "Coffee Shop": coffee_shop_stateful_metrics,
                    "Consumer": consumer_stateful_metrics}
