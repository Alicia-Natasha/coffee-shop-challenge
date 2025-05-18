from customer import Customer
from coffee import Coffee

class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer class")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee class")
        if not isinstance(price, float):
            raise ValueError("Price must be a float")
        if not(1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order._all_orders.append(self)

    @property
    def price(self):
        return self._price
    @property
    def coffee(self):
        return self._coffee
    @property
    def customer(self):
        return self._customer
    
    @classmethod
    def all_orders(cls):
        return cls._all_orders