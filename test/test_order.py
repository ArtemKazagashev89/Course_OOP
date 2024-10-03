def test_order_init(order1):
    assert order1.purchased == 2
    assert order1.total_cost == 360000


def test_order_str(order1):
    assert str(order1) == "Продан Samsung Galaxy S23 Ultra в количестве 2шт. на сумму 360000.0"
