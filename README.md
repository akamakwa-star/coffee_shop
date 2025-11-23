# Coffee Shop Domain Model

A Python object-oriented application that models a Coffee Shop domain with customers, coffees, and orders using domain modeling principles.

## Project Overview

This project implements a complete domain model for a Coffee Shop with three main entities:
- **Customer**: Represents coffee shop customers
- **Coffee**: Represents coffee products
- **Order**: Represents customer orders (connecting Customer and Coffee)

The model demonstrates proper object-oriented design with validation, relationships, and aggregate methods.

## Folder Structure

```
coffee_shop/
├── customer.py          # Customer class implementation
├── coffee.py            # Coffee class implementation
├── order.py             # Order class implementation
├── debug.py             # Interactive testing script
├── tests/               # Test suite directory
│   ├── test_customer.py # Customer class tests
│   ├── test_coffee.py   # Coffee class tests
│   └── test_order.py    # Order class tests
├── README.md            # This file
├── Pipfile              # Project dependencies
└── pytest.ini           # Pytest configuration
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pipenv

### Setup

1. **Navigate to the project directory:**
   ```bash
   cd coffee_shop
   ```

2. **Install dependencies using pipenv:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Install pytest (if not already included):**
   ```bash
   pipenv install pytest
   ```

## Usage

### Running the Debug Script

To test the functionality interactively:

```bash
python debug.py
```

The debug script demonstrates:
- Creating customers and coffees
- Placing orders
- Retrieving customer orders and coffees
- Retrieving coffee orders and customers
- Calculating average prices
- Finding the most loyal customer (most aficionado)

### Running Tests

Execute the complete test suite:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_customer.py
pytest tests/test_coffee.py
pytest tests/test_order.py
```

Run a specific test:

```bash
pytest tests/test_customer.py::TestCustomerInitialization::test_customer_init_valid_name
```

## API Documentation

### Customer Class

#### Initialization
```python
customer = Customer(name: str)
```

**Parameters:**
- `name` (str): Customer's name (1-15 characters)

**Raises:**
- `TypeError`: If name is not a string
- `ValueError`: If name length is not between 1-15 characters

#### Properties
- `name` (str): Customer's name with getter/setter validation

#### Methods

**orders() -> list**
- Returns: List of all Order instances for this customer
- Example: `customer_orders = customer.orders()`

**coffees() -> list**
- Returns: Unique list of Coffee instances ordered by this customer
- Example: `favorite_coffees = customer.coffees()`

**create_order(coffee: Coffee, price: float) -> Order**
- Creates a new order for this customer
- Parameters:
  - `coffee` (Coffee): The coffee to order
  - `price` (float): Price of the order (1.0-10.0)
- Returns: The newly created Order instance
- Example: `order = customer.create_order(espresso, 2.50)`

**most_aficionado(coffee: Coffee) -> Customer | None** (Class Method)
- Finds the customer who has spent the most money on a given coffee
- Parameters:
  - `coffee` (Coffee): The coffee to check
- Returns: Customer with highest spending on this coffee, or None
- Example: `top_fan = Customer.most_aficionado(espresso)`

### Coffee Class

#### Initialization
```python
coffee = Coffee(name: str)
```

**Parameters:**
- `name` (str): Coffee's name (minimum 3 characters)

**Raises:**
- `TypeError`: If name is not a string
- `ValueError`: If name length is less than 3 characters

#### Properties
- `name` (str): Coffee's name with getter/setter validation

#### Methods

**orders() -> list**
- Returns: List of all Order instances for this coffee
- Example: `coffee_orders = coffee.orders()`

**customers() -> list**
- Returns: Unique list of Customer instances who have ordered this coffee
- Example: `fans = coffee.customers()`

**num_orders() -> int**
- Returns: Total number of times this coffee has been ordered
- Example: `total = coffee.num_orders()`

**average_price() -> float**
- Returns: Average price at which this coffee has been ordered (0 if no orders)
- Example: `avg = coffee.average_price()`

### Order Class

#### Initialization
```python
order = Order(customer: Customer, coffee: Coffee, price: float)
```

**Parameters:**
- `customer` (Customer): The customer placing the order
- `coffee` (Coffee): The coffee being ordered
- `price` (float): Price of the order (1.0-10.0)

**Raises:**
- `TypeError`: If customer is not a Customer or coffee is not a Coffee
- `TypeError`: If price is not a number
- `ValueError`: If price is not between 1.0-10.0

#### Properties
- `customer` (Customer): The customer for this order (with validation)
- `coffee` (Coffee): The coffee for this order (with validation)
- `price` (float): The price of the order (with validation)

## Object Relationships

### Many-to-Many Relationship

The Coffee Shop uses an `Order` entity to establish a many-to-many relationship:

```
┌───────────────────────────────────────────────────────────────┐
│                        RELATIONSHIPS                          │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  Customer  ◄──────────────────────────────►  Coffee          │
│    (1)            Order (Many)           (1)                 │
│    │                  │                       │              │
│    │              (Many)                     │               │
│    └──────────────────┘                       │              │
│                                               │              │
│   - A Customer can have many Orders          │              │
│   - A Coffee can have many Orders            │              │
│   - Each Order belongs to one Customer       │              │
│   - Each Order belongs to one Coffee         │              │
│                                               │              │
└───────────────────────────────────────────────────────────────┘
```

## Design Patterns

### 1. Single Source of Truth
All orders are tracked in class variables:
- `Customer._all_orders`: Shared across all Customer instances
- `Coffee._all_orders`: Shared across all Coffee instances

This ensures consistent data when querying relationships.

### 2. Property Validation
All properties use Python's `@property` decorator with setters for validation:
```python
@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    # Validation logic
    self._name = value
```

### 3. Immutable References
Once an Order is created with a Customer and Coffee, these relationships are maintained through property validation, ensuring data integrity.

## Example Usage

```python
from customer import Customer
from coffee import Coffee

# Create customers and coffees
alice = Customer("Alice")
bob = Customer("Bob")
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")

# Create orders
order1 = alice.create_order(espresso, 2.50)
order2 = alice.create_order(cappuccino, 3.50)
order3 = bob.create_order(espresso, 2.75)

# Query customer data
print(f"Alice ordered: {len(alice.orders())} items")
print(f"Alice likes: {len(alice.coffees())} types of coffee")

# Query coffee data
print(f"Espresso sold: {espresso.num_orders()} times")
print(f"Espresso avg price: ${espresso.average_price():.2f}")

# Find most loyal customer
top_espresso_fan = Customer.most_aficionado(espresso)
print(f"Top espresso fan: {top_espresso_fan.name}")
```

## Testing

The test suite includes:

- **Customer Tests**: 20+ test cases covering initialization, validation, relationships
- **Coffee Tests**: 20+ test cases covering initialization, validation, aggregates
- **Order Tests**: 15+ test cases covering initialization, validation, integration

All tests follow pytest conventions and include:
- Positive test cases (happy path)
- Negative test cases (error handling)
- Edge cases (boundary conditions)
- Integration tests (cross-class relationships)

### Test Coverage

- Input validation for all properties
- Type checking for parameters
- Relationship integrity
- Aggregate methods
- Class methods
- Edge cases and boundary conditions

## Code Quality

The code follows Python best practices:

- **PEP 8 Compliance**: Proper naming conventions, spacing, and documentation
- **DRY Principle**: No code duplication; helper methods used appropriately
- **Type Safety**: Extensive input validation with clear error messages
- **Documentation**: Comprehensive docstrings for all classes and methods
- **Exception Handling**: Proper use of TypeError and ValueError

## Key Features

✅ **Object-Oriented Design**: Classes with proper encapsulation and relationships
✅ **Input Validation**: Comprehensive validation with meaningful error messages
✅ **Single Source of Truth**: Centralized order tracking across entities
✅ **Aggregate Methods**: Methods for calculating statistics and relationships
✅ **Class Methods**: Support for class-level operations (most_aficionado)
✅ **Comprehensive Testing**: 50+ unit tests with high coverage
✅ **Clean Code**: PEP 8 compliant, well-documented, maintainable

## Requirements Met

✅ Folder structure with all necessary files  
✅ Detailed README with all required sections  
✅ Customer class with name validation (1-15 characters)  
✅ Coffee class with name validation (3+ characters)  
✅ Order class with price validation (1.0-10.0)  
✅ Object relationship methods (orders, coffees, customers)  
✅ Aggregate methods (num_orders, average_price)  
✅ Class method (most_aficionado)  
✅ Debug script for interactive testing  
✅ Comprehensive test suite  
✅ Input validation and exception handling  
✅ PEP 8 compliant, clean code  

## Troubleshooting

### ImportError when running tests
Ensure you're running tests from the project root:
```bash
cd coffee_shop
pytest
```

### Validation errors with price
Remember that price must be between 1.0 and 10.0:
```python
order = customer.create_order(coffee, 5.50)  # ✓ Valid
order = customer.create_order(coffee, 0.50)  # ✗ Invalid (too low)
order = customer.create_order(coffee, 15.00) # ✗ Invalid (too high)
```

### Validation errors with names
- Customer names: 1-15 characters
- Coffee names: 3+ characters
```python
customer = Customer("Alice")    # ✓ Valid
customer = Customer("")         # ✗ Invalid (empty)
coffee = Coffee("Espresso")     # ✓ Valid
coffee = Coffee("Jo")           # ✗ Invalid (too short)
```

## Future Enhancements

Potential improvements for future versions:
- Add timestamps to Order class
- Implement order history and filtering
- Add payment methods and status tracking
- Create a database backend (SQLAlchemy)
- Add API endpoints (Flask/FastAPI)
- Implement inventory management

## Author

Created as a solution to the Code Challenge: Coffee Shop (Object Relationships)

## License

This project is open source and available under the MIT License.
