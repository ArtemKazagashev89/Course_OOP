import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.product_iteration import ProductIteration
from src.smartphone import Smartphone


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    """Данные для теста класса Product"""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=["product1", "product2", "product3"],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=["product4"],
    )


@pytest.fixture
def data_for_counters_categories():
    """Данные для теста класса Category"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для " "удобства жизни",
        [
            Product.new_product(
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
            ),
            Product.new_product(
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
            ),
        ],
    )


@pytest.fixture
def data_for_categories():
    """Данные для теста класса Category для проверки корректности инициализации"""
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )


@pytest.fixture
def new_product():
    """Новый продукт для теста Category - добавление нового продукта в список"""
    return Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


@pytest.fixture
def data_for_err():
    """Для проверки возбуждения ошибки при добавлении нового токара в список"""
    return "Новый продукт"


@pytest.fixture
def product_iterator(data_for_counters_categories):
    return ProductIteration(data_for_counters_categories)


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def product_invalid():
    return Product("Бракованный товар", "Неверное количество", 1000.0, 0)


@pytest.fixture
def category1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    return category1
