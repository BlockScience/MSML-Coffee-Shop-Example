from .system import system_state
from .coffee_shop import coffee_shop_state
from .consumer import consumer_state

state = {"System": system_state,
         "Coffee Shop": coffee_shop_state,
         "Consumer": consumer_state}
