# Coffee Shop Challenge

## Project Structure
coffee-shop-challenge/
├── customer.py
├── coffee.py
├── order.py
├── tests/
│   └── coffee_test.py
├── README.md

## Features 
Create customers and coffees with validation.

Place orders linking customers and coffees with prices.

Retrieve:
1. All orders for a customer or coffee.
2. Unique coffees a customer has tried.
3. Unique customers who’ve tried a specific coffee.
4. Total number of orders and average price for each coffee.
5. Customer who spent the most on a specific coffee.

## Overview
### Customer
name: str (1–15 characters)
orders() → List of Order instances
coffees() → Unique Coffee instances they've ordered
create_order(coffee, price) → Creates a new Order
most_aficionado(coffee) (class method) → Customer who spent the most on a given coffee

### Coffee
name: str (min 3 characters)
orders() → List of Order instances
customers() → Unique Customer instances
number_of_orders() → int
average_price() → float

### Order
price: float (1.0–10.0), immutable
customer: Customer instance
coffee: Coffee instance
all_orders() → Class method to access all Order instances

## Author 
Alicia Natasha

## License
This project is licensed under the [MIT License](LICENSE).