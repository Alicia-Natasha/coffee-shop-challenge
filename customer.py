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
        return self._name   
    
    def orders(self):
        return [order for order in Order.all_orders() if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})    
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    def most_aficionado(cls, coffee):
        customer_spending = {}

        for order in Order.all_orders():
            if order.coffee == coffee:
                customer = order.customer
                customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        if not customer_spending:
            return None
        
        return max(customer_spending, key=customer_spending.get)