from typing import Union

from homework11.task02.task02 import DiscountStrategy, Order


class MorningDiscount(DiscountStrategy):
    def final_price(self, price: Union[float, int]):
        return price - price * 0.5


class ElderDiscount(DiscountStrategy):
    def final_price(self, price: Union[float, int]):
        return price - price * 0.9


def test_count_discount():
    order = Order(100, MorningDiscount())
    assert order.final_price() == 50

    order.discount_strategy = ElderDiscount()
    assert order.final_price() == 10
