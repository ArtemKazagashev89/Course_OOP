from src.base_category import BaseCategory
from src.product import Product


class Order(BaseCategory):

    def __init__(self, product, purchased):
        self.product = product
        self.purchased = purchased
        self.total_cost = product.price * self.purchased
        self.product.quantity -= self.purchased

    def __str__(self):
        return f"Продан {self.product.name} в количестве {self.purchased}шт. на сумму {self.total_cost}"


if __name__ == "__main__":
    order1 = Order(Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5), 2)

    print(str(order1))
    print(order1.product.quantity)
