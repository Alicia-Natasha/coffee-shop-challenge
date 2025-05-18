from customer import Customer
from order import Order

class Coffee:
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (3 <= len(name)):
            raise ValueError("Name must be at least 3 characters")
        self._name = name

    def name(self):
        return self._name
    
    def order(self):
        return [order for order in Order.all_orders() if order.coffee == self]
    
    def customers(self):
        return [order.customer for order in self.orders()]
    
    