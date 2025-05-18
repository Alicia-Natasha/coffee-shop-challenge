from customer import Customer
from order import Order

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = name

    @property
    def name(self):
        return self._name
    
    def orders(self):
        return [order for order in Order.all_orders() if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def number_of_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not self.orders():
            return 0.0
        total_price = sum(order.price for order in orders)
        return total_price / len(self.orders())