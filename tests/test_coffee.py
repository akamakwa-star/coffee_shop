
"""Tests for the Coffee class."""

import pytest
import sys
import os

# Add parent directory to path to import our classes
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order


class TestCoffeeInitialization:
    """Tests for Coffee initialization and properties."""
    
    def test_coffee_init_valid_name(self):
        """Test creating a coffee with a valid name."""
        coffee = Coffee("Espresso")
        assert coffee.name == "Espresso"
    
    def test_coffee_name_valid_length_min(self):
        """Test coffee name with minimum valid length (3)."""
        coffee = Coffee("Foo")
        assert coffee.name == "Foo"
    
    def test_coffee_name_too_short(self):
        """Test that a name shorter than 3 characters raises ValueError."""
        with pytest.raises(ValueError):
            Coffee("Jo")
    
    def test_coffee_name_empty(self):
        """Test that an empty name raises ValueError."""
        with pytest.raises(ValueError):
            Coffee("")
    
    def test_coffee_name_not_string(self):
        """Test that a non-string name raises TypeError."""
        with pytest.raises(TypeError):
            Coffee(123)
    
    def test_coffee_name_not_string_none(self):
        """Test that None as name raises TypeError."""
        with pytest.raises(TypeError):
            Coffee(None)
    
    def test_coffee_name_long(self):
        """Test that long coffee names are accepted."""
        long_name = "Very Long Coffee Name With Many Characters"
        coffee = Coffee(long_name)
        assert coffee.name == long_name


class TestCoffeeMethods:
    """Tests for Coffee methods."""
    
    def setup_method(self):
        """Reset order tracking before each test."""
        Customer._all_orders = []
        Coffee._all_orders = []
    
    def test_coffee_orders_empty(self):
        """Test that a new coffee has no orders."""
        coffee = Coffee("Espresso")
        assert coffee.orders() == []
    
    def test_coffee_orders_single(self):
        """Test retrieving a single order for a coffee."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = customer.create_order(coffee, 2.5)
        
        orders = coffee.orders()
        assert len(orders) == 1
        assert orders[0] == order
    
    def test_coffee_orders_multiple(self):
        """Test retrieving multiple orders for a coffee."""
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        
        order1 = customer1.create_order(coffee, 2.5)
        order2 = customer2.create_order(coffee, 3.0)
        
        orders = coffee.orders()
        assert len(orders) == 2
        assert order1 in orders
        assert order2 in orders
    
    def test_coffee_customers_empty(self):
        """Test that a new coffee has no customers."""
        coffee = Coffee("Espresso")
        assert coffee.customers() == []
    
    def test_coffee_customers_single(self):
        """Test retrieving a single customer for a coffee."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        customer.create_order(coffee, 2.5)
        
        customers = coffee.customers()
        assert len(customers) == 1
        assert customer in customers
    
    def test_coffee_customers_multiple_unique(self):
        """Test that customers() returns unique customers."""
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        
        customer1.create_order(coffee, 2.5)
        customer1.create_order(coffee, 3.0)
        customer2.create_order(coffee, 4.0)
        
        customers = coffee.customers()
        assert len(customers) == 2
        assert customer1 in customers
        assert customer2 in customers
    
    def test_num_orders_zero(self):
        """Test num_orders returns 0 for a coffee with no orders."""
        coffee = Coffee("Espresso")
        assert coffee.num_orders() == 0
    
    def test_num_orders_single(self):
        """Test num_orders with a single order."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        customer.create_order(coffee, 2.5)
        
        assert coffee.num_orders() == 1
    
    def test_num_orders_multiple(self):
        """Test num_orders with multiple orders."""
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        
        customer1.create_order(coffee, 2.5)
        customer1.create_order(coffee, 3.0)
        customer2.create_order(coffee, 4.0)
        
        assert coffee.num_orders() == 3
    
    def test_average_price_zero(self):
        """Test average_price returns 0 for a coffee with no orders."""
        coffee = Coffee("Espresso")
        assert coffee.average_price() == 0
    
    def test_average_price_single(self):
        """Test average_price with a single order."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        customer.create_order(coffee, 2.5)
        
        assert coffee.average_price() == 2.5
    
    def test_average_price_multiple(self):
        """Test average_price with multiple orders."""
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        
        customer1.create_order(coffee, 2.0)
        customer1.create_order(coffee, 4.0)
        customer2.create_order(coffee, 6.0)
        
        # Average: (2.0 + 4.0 + 6.0) / 3 = 4.0
        assert coffee.average_price() == 4.0
    
    def test_average_price_different_coffees(self):
        """Test that average_price only considers this coffee."""
        customer = Customer("Alice")
        espresso = Coffee("Espresso")
        cappuccino = Coffee("Cappuccino")
        
        customer.create_order(espresso, 2.0)
        customer.create_order(espresso, 4.0)
        customer.create_order(cappuccino, 10.0)
        
        # Espresso average: (2.0 + 4.0) / 2 = 3.0
        # Cappuccino average: 10.0
        assert espresso.average_price() == 3.0
        assert cappuccino.average_price() == 10.0


class TestCoffeeNameUpdate:
    """Tests for updating coffee name."""
    
    def test_update_name_valid(self):
        """Test updating a coffee's name to a valid value."""
        coffee = Coffee("Espresso")
        coffee.name = "Americano"
        assert coffee.name == "Americano"
    
    def test_update_name_invalid_length(self):
        """Test updating name to invalid length raises ValueError."""
        coffee = Coffee("Espresso")
        with pytest.raises(ValueError):
            coffee.name = "Jo"
    
    def test_update_name_not_string(self):
        """Test updating name to non-string raises TypeError."""
        coffee = Coffee("Espresso")
        with pytest.raises(TypeError):
            coffee.name = 123
