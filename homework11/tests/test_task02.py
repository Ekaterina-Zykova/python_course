from homework11.task02.task02 import Order


def morning_discount(order):
    return order - order * 0.5


def elder_discount(order):
    return order - order * 0.9


def test_count_discount():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50

    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10

    order_3 = Order(100)
    assert order_3.final_price() == 75
