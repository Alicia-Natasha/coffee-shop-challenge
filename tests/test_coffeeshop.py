import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    assert Customer("Alice").name == "Alice"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")
    assert Coffee("Latte").name == "Latte"

def test_create_order_and_relationships():
    customer = Customer("Bob")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 4.5)

    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

    assert order in customer.orders()
    assert coffee in customer.coffees()
    assert order in coffee.orders()
    assert customer in coffee.customers()

def test_average_price_and_num_orders():
    customer = Customer("Eve")
    coffee = Coffee("Mocha")
    Order(customer, coffee, 3.0)
    Order(customer, coffee, 5.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.0

def test_most_aficionado():
    customer1 = Customer("Tom")
    customer2 = Customer("Jerry")
    coffee = Coffee("Cappuccino")

    Order(customer1, coffee, 3.0)
    Order(customer2, coffee, 6.0)
    Order(customer2, coffee, 2.0)

    assert Customer.most_aficionado(coffee) == customer2
