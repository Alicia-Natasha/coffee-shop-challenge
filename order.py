from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(price, float):
            raise ValueError("Price must be a float")
        if not(1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def price(self):
        return self._price