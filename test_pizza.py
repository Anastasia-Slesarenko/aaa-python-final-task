import pytest
from pizza import Pizza, Margherita, Pepperoni, Hawaiian


def test_create_pizza():
    pizza = Pizza()
    assert pizza.size == "L"


def test_create_pizza_with_custom_size():
    pizza = Pizza(size="XL")
    assert pizza.size == "XL"


def test_create_pizza_with_invalid_size():
    with pytest.raises(ValueError):
        Pizza(size="S")


def test_pizza_equality():
    pizza1 = Margherita()
    pizza2 = Margherita()
    assert pizza1 == pizza2


def test_different_pizzas_not_equal():
    pizza1 = Hawaiian()
    pizza2 = Pepperoni()
    assert pizza1 != pizza2


if __name__ == "__main__":
    test_create_pizza()
