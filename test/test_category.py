from src.category import Category
from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert first_category.product_count == 4
    assert second_category.product_count == 4
    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_add_product():
    """Тестируем добавление продукта в категорию."""
    category = Category("Смартфоны", "Смартфоны, как средство коммуникации")
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category.add_product(product4)

    assert len(category.products) == 1
    assert category.products[0].name == '55" QLED 4K'


def test_products_list(sample_products):
    """Тестируем вывод списка продуктов."""
    category = Category("Смартфоны", "Смартфоны, как средство коммуникации", sample_products)

    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0. Остаток: 5\n"
        "Iphone 15, 210000.0. Остаток: 8\n"
        "Xiaomi Redmi Note 11, 31000.0. Остаток: 14\n"
    )

    assert category.products_list == expected_output


def test_category_count(sample_products):
    """Тестируем счетчик категорий."""
    category1 = Category("Смартфоны", "Описание")
    category2 = Category("Телевизоры", "Описание")

    assert Category.category_count == 2
