from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс, представляющий продукт."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if self.quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, param_product):
        return cls(**param_product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        """Метод меняющий цену продукта в зависимости от условия"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price > self.__price:
            self.__price = new_price
        else:
            while True:
                answer = input("Введите ответ на понижение цены - y/n: ")
                if answer.lower() == "y":
                    self.__price = new_price
                    break
                elif answer.lower() == "n":
                    break


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")
