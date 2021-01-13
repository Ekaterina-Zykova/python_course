"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from abc import ABC, abstractmethod
from typing import Union


class DiscountStrategy(ABC):
    @abstractmethod
    def final_price(self, price: Union[float, int]):
        pass


class Order:
    def __init__(self, price: Union[float, int], discount: DiscountStrategy) -> None:
        self.price = price
        self._discount = discount

    @property
    def discount_strategy(self) -> DiscountStrategy:
        return self._discount

    @discount_strategy.setter
    def discount_strategy(self, discount: DiscountStrategy) -> None:
        self._discount = discount

    def final_price(self) -> Union[float, int]:
        return self._discount.final_price(self.price)
