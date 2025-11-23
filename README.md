
Coffee Shop Domain Model

A Python OOP project that models a Coffee Shop using three core classes: Customer, Coffee, and Order. The system demonstrates relationships, validation, and domain logic using object-oriented design.

Overview

Customer: Can place many orders

Coffee: Can have many orders

Order: Connects a Customer and a Coffee (many-to-many relationship)

Includes validation, relationship methods, aggregate functions, and a class method to find the top-spending customer for a given coffee.

Project Structure
coffee_shop/
├── customer.py
├── coffee.py
├── order.py
├── debug.py
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
├── Pipfile
├── pytest.ini
└── README.md

Setup
cd coffee_shop
pipenv install
pipenv shell
pipenv install pytest

Usage

Run the debug script:

python debug.py


Run all tests:

pytest

Class Features
Customer

Validates name (1–15 chars)

orders(): all orders for the customer

coffees(): unique coffees ordered

create_order(coffee, price)

most_aficionado(coffee): customer who spent the most on that coffee

Coffee

Validates name (≥3 chars)

orders(): all orders for the coffee

customers(): unique customers

num_orders(): total orders

average_price(): average price

Order

Validates customer, coffee, and price (1.0–10.0)

Tracks all orders in a class-level list

Example
alice = Customer("Alice")
espresso = Coffee("Espresso")
alice.create_order(espresso, 3.5)

print(espresso.num_orders())          # 1
print(espresso.average_price())       # 3.5
print(Customer.most_aficionado(espresso).name)

Requirements Met

Full OOP implementation

Validations & error handling

Relationship & aggregation methods

Class method (most_aficionado)

Tests included

PEP 8 compliant