class Product:
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
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))
