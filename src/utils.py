import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Читает JSON файл и возвращает его содержимое в виде словаря."""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_object_from_json(data):
    """Создает объекты Product и Category из данных, загруженных из JSON."""
    products = []
    for product in data:
        items = []
        for item in product["products"]:
            products.append(Product(**item))
        product["products"] = items
        products.append(Category(**product))
    return products


if __name__ == "__main__":
    data_product = read_json("../data/products.json")
    product_data = create_object_from_json(data_product)

    print(product_data[0].name)
    print(product_data[0].description)
