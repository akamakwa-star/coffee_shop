
"""Tests for the Customer class."""

import pytest
import sys
import os

# Add parent directory to path to import our classes
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order


class TestCustomerInitialization:
    """Tests for Customer initialization and properties."""
    
    def test_customer_init_valid_name(self):
        """Test creating a customer with a valid name."""
        customer = Customer("Alice")
        assert customer.name == "Alice"
    
    def test_customer_name_valid_length_min(self):
        """Test customer name with minimum valid length (1)."""
        customer = Customer("A")
        assert customer.name == "A"
    
    def test_customer_name_valid_length_max(self):
        """Test customer name with maximum valid length (15)."""
        customer = Customer("A" * 15)
        assert customer.name == "A" * 15
    
    def test_customer_name_too_long(self):
        """Test that a name longer than 15 characters raises ValueError."""
        with pytest.raises(ValueError):
            Customer("A" * 16)
    
    def test_customer_name_empty(self):
        """Test that an empty name raises ValueError."""
        with pytest.raises(ValueError):
            Customer("")
    
    def test_customer_name_not_string(self):
        """Test that a non-string name raises TypeError."""
        with pytest.raises(TypeError):
            Customer(123)
    
    def test_customer_name_not_string_none(self):
        """Test that None as name raises TypeError."""
        with pytest.raises(TypeError):
            Customer(None)


class TestCustomerMethods:
    """Tests for Customer methods."""
    
    def setup_method(self):
        """Reset order tracking before each test."""
        Customer._all_orders = []
        Coffee._all_orders = []
    
    def test_customer_orders_empty(self):
        """Test that a new customer has no orders."""
        customer = Customer("Alice")
        assert customer.orders() == []
    
    def test_customer_orders_single(self):
        """Test retrieving a single order for a customer."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = customer.create_order(coffee, 2.5)
        
        orders = customer.orders()
        assert len(orders) == 1
        assert orders[0] == order
    
    def test_customer_orders_multiple(self):
        """Test retrieving multiple orders for a customer."""
        customer = Customer("Alice")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Cappuccino")
        
        order1 = customer.create_order(coffee1, 2.5)
        order2 = customer.create_order(coffee2, 3.0)
        
        orders = customer.orders()
        assert len(orders) == 2
        assert order1 in orders
        assert order2 in orders
    
    def test_customer_coffees_empty(self):
        """Test that a new customer has ordered no coffees."""
        customer = Customer("Alice")
        assert customer.coffees() == []
    
    def test_customer_coffees_single(self):
        """Test retrieving a single coffee for a customer."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        customer.create_order(coffee, 2.5)
        
        coffees = customer.coffees()
        assert len(coffees) == 1
        assert coffee in coffees
    
    def test_customer_coffees_multiple_unique(self):
        """Test that coffees() returns unique coffees."""
        customer = Customer("Alice")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Cappuccino")
        
        customer.create_order(coffee1, 2.5)
        customer.create_order(coffee1, 3.0)
        customer.create_order(coffee2, 4.0)
        
        coffees = customer.coffees()
        assert len(coffees) == 2
        assert coffee1 in coffees
        assert coffee2 in coffees
    
    def test_create_order(self):
        """Test creating an order through a customer."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = customer.create_order(coffee, 2.5)
        
        assert isinstance(order, Order)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 2.5
    
    def test_most_aficionado_single_customer(self):
        """Test most_aficionado with a single customer."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        customer.create_order(coffee, 2.5)
        customer.create_order(coffee, 3.0)
        
        most_fan = Customer.most_aficionado(coffee)
        assert most_fan == customer
    
    def test_most_aficionado_multiple_customers(self):
        """Test most_aficionado with multiple customers."""
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        
        customer1.create_order(coffee, 2.0)
        customer1.create_order(coffee, 2.5)  # Total: 4.5
        customer2.create_order(coffee, 3.0)  # Total: 3.0
        
        most_fan = Customer.most_aficionado(coffee)
        assert most_fan == customer1
    
    def test_most_aficionado_no_customers(self):
        """Test most_aficionado with no orders returns None."""
        coffee = Coffee("Espresso")
        most_fan = Customer.most_aficionado(coffee)
        assert most_fan is None
    
    def test_most_aficionado_different_coffees(self):
        """Test most_aficionado only considers specific coffee."""
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        espresso = Coffee("Espresso")
        cappuccino = Coffee("Cappuccino")
        
        customer1.create_order(espresso, 2.0)
        customer2.create_order(cappuccino, 5.0)
        customer2.create_order(cappuccino, 4.5)  # Spent 9.5 on cappuccino
        
        espresso_fan = Customer.most_aficionado(espresso)
        cappuccino_fan = Customer.most_aficionado(cappuccino)
        
        assert espresso_fan == customer1
        assert cappuccino_fan == customer2


class TestCustomerNameUpdate:
    """Tests for updating customer name."""
    
    def test_update_name_valid(self):
        """Test updating a customer's name to a valid value."""
        customer = Customer("Alice")
        customer.name = "Bob"
        assert customer.name == "Bob"
    
    def test_update_name_invalid_length(self):
        """Test updating name to invalid length raises ValueError."""
        customer = Customer("Alice")
        with pytest.raises(ValueError):
            customer.name = "A" * 20
    
    def test_update_name_not_string(self):
        """Test updating name to non-string raises TypeError."""
        customer = Customer("Alice")
        with pytest.raises(TypeError):
            customer.name = 123
