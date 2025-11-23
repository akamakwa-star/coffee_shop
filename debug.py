
"""
Debug script for testing the Coffee Shop domain model.
Use this file to interactively test the functionality of Customer, Coffee, and Order classes.
"""

from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
print("=" * 50)
print("Creating Customers")
print("=" * 50)

customer1 = Customer("Alice")
customer2 = Customer("Bob")
customer3 = Customer("Charlie")

print(f"Customer 1: {customer1.name}")
print(f"Customer 2: {customer2.name}")
print(f"Customer 3: {customer3.name}")

# Create some coffees
print("\n" + "=" * 50)
print("Creating Coffees")
print("=" * 50)

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Cappuccino")
coffee3 = Coffee("Latte")

print(f"Coffee 1: {coffee1.name}")
print(f"Coffee 2: {coffee2.name}")
print(f"Coffee 3: {coffee3.name}")

# Create some orders
print("\n" + "=" * 50)
print("Creating Orders")
print("=" * 50)

# Alice orders
order1 = customer1.create_order(coffee1, 2.5)
print(f"Order 1: {order1.customer.name} ordered {order1.coffee.name} for ${order1.price}")

order2 = customer1.create_order(coffee1, 3.0)
print(f"Order 2: {order2.customer.name} ordered {order2.coffee.name} for ${order2.price}")

order3 = customer1.create_order(coffee2, 4.0)
print(f"Order 3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price}")

# Bob orders
order4 = customer2.create_order(coffee1, 2.5)
print(f"Order 4: {order4.customer.name} ordered {order4.coffee.name} for ${order4.price}")

order5 = customer2.create_order(coffee2, 4.5)
print(f"Order 5: {order5.customer.name} ordered {order5.coffee.name} for ${order5.price}")

# Charlie orders
order6 = customer3.create_order(coffee1, 2.0)
print(f"Order 6: {order6.customer.name} ordered {order6.coffee.name} for ${order6.price}")

# Test Customer methods
print("\n" + "=" * 50)
print("Testing Customer Methods")
print("=" * 50)

print(f"\nAlice's orders: {len(customer1.orders())}")
for order in customer1.orders():
    print(f"  - {order.coffee.name}: ${order.price}")

print(f"\nAlice's coffees: {len(customer1.coffees())}")
for coffee in customer1.coffees():
    print(f"  - {coffee.name}")

# Test Coffee methods
print("\n" + "=" * 50)
print("Testing Coffee Methods")
print("=" * 50)

print(f"\nEspresso orders: {coffee1.num_orders()}")
for order in coffee1.orders():
    print(f"  - {order.customer.name}: ${order.price}")

print(f"\nEspresso customers: {len(coffee1.customers())}")
for customer in coffee1.customers():
    print(f"  - {customer.name}")

print(f"\nEspresso average price: ${coffee1.average_price():.2f}")
print(f"Cappuccino average price: ${coffee2.average_price():.2f}")
print(f"Latte average price: ${coffee3.average_price():.2f}")

# Test most_aficionado class method
print("\n" + "=" * 50)
print("Testing most_aficionado Class Method")
print("=" * 50)

most_espresso_fan = Customer.most_aficionado(coffee1)
print(f"\nCustomer who spent most on Espresso: {most_espresso_fan.name}")

most_cappuccino_fan = Customer.most_aficionado(coffee2)
print(f"Customer who spent most on Cappuccino: {most_cappuccino_fan.name}")

most_latte_fan = Customer.most_aficionado(coffee3)
print(f"Customer who spent most on Latte: {most_latte_fan}")

# Test validation errors
print("\n" + "=" * 50)
print("Testing Validation")
print("=" * 50)

try:
    invalid_customer = Customer("a" * 20)  # Name too long
except ValueError as e:
    print(f"✓ Caught expected error for long name: {e}")

try:
    invalid_coffee = Coffee("Jo")  # Name too short
except ValueError as e:
    print(f"✓ Caught expected error for short coffee name: {e}")

try:
    invalid_order = Order(customer1, coffee1, 15.0)  # Price too high
except ValueError as e:
    print(f"✓ Caught expected error for high price: {e}")

try:
    invalid_order = Order(customer1, coffee1, 0.5)  # Price too low
except ValueError as e:
    print(f"✓ Caught expected error for low price: {e}")

print("\n" + "=" * 50)
print("Debug script completed successfully!")
print("=" * 50)
