from src.product import Product
import pytest
def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5



def test_product_initialization():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_setter_positive():
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_product_price_setter_negative():
    product = Product("Test Product", "Test Description", 100.0, 10)

    # Здесь у нас нет возможности ввести данные, поэтому просто проверяем, что цена не меняется
    product.price = -50
    assert product.price == 100.0


def test_product_price_setter_zero():
    product = Product("Test Product", "Test Description", 100.0, 10)

    # Здесь у нас нет возможности ввести данные, поэтому просто проверяем, что цена не меняется
    product.price = 0
    assert product.price == 100.0


def test_product_new_product():
    param_product = {
        "name": "New Product",
        "description": "New Description",
        "price": 200.0,
        "quantity": 5
    }
    product = Product.new_product(param_product)
    assert product.name == "New Product"
    assert product.price == 200.0
