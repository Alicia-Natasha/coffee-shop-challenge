from order import Order
from coffee import Coffee

class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self.name   
    
    def order(self):
        return [order for order in Order.all_orders() if order.customer == self]
    
    def coffee(self):
        return [order.coffee for order in self.orders()]    

