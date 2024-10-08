import pytest


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


def test_category_products_property(data_for_counters_categories):
    """Проверка корректности вывода строки"""
    assert data_for_counters_categories.products == (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_add_product(data_for_categories, new_product, data_for_err):
    """Проверка добавления нового продукта в список"""
    assert len(data_for_categories.products_in_list) == 1
    data_for_categories.add_product(new_product)
    assert len(data_for_categories.products_in_list) == 2
    with pytest.raises(TypeError):
        data_for_categories.add_product(data_for_err)


def test_category_str(data_for_counters_categories):
    assert str(data_for_counters_categories) == "Смартфоны, количество продуктов: 22 шт."


def test_middle_price(category1):
    assert category1.middle_price() == 140333.33333333334


def test_middle_price_empy(product_invalid):
    assert product_invalid.middle_price() == 0
