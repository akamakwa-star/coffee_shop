
"""Tests for the Order class."""

import pytest
import sys
import os

# Add parent directory to path to import our classes
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order


class TestOrderInitialization:
    """Tests for Order initialization and properties."""
    
    def setup_method(self):
        """Reset order tracking before each test."""
        Customer._all_orders = []
        Coffee._all_orders = []
    
    def test_order_init_valid(self):
        """Test creating an order with valid parameters."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 2.5)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 2.5
    
    def test_order_customer_type_check(self):
        """Test that order requires a Customer instance."""
        coffee = Coffee("Espresso")
        with pytest.raises(TypeError):
            Order("Not a customer", coffee, 2.5)
    
    def test_order_coffee_type_check(self):
        """Test that order requires a Coffee instance."""
        customer = Customer("Alice")
        with pytest.raises(TypeError):
            Order(customer, "Not a coffee", 2.5)
    
    def test_order_price_valid_minimum(self):
        """Test order with minimum valid price (1.0)."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 1.0)
        assert order.price == 1.0
    
    def test_order_price_valid_maximum(self):
        """Test order with maximum valid price (10.0)."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 10.0)
        assert order.price == 10.0
    
    def test_order_price_valid_middle(self):
        """Test order with a middle-range valid price."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 5.5)
        assert order.price == 5.5
    
    def test_order_price_too_low(self):
        """Test that a price below 1.0 raises ValueError."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.99)
    
    def test_order_price_too_high(self):
        """Test that a price above 10.0 raises ValueError."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        with pytest.raises(ValueError):
            Order(customer, coffee, 10.01)
    
    def test_order_price_zero(self):
        """Test that a price of 0 raises ValueError."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        with pytest.raises(ValueError):
            Order(customer, coffee, 0)
    
    def test_order_price_negative(self):
        """Test that a negative price raises ValueError."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        with pytest.raises(ValueError):
            Order(customer, coffee, -5.0)
    
    def test_order_price_not_number(self):
        """Test that a non-numeric price raises TypeError."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        with pytest.raises(TypeError):
            Order(customer, coffee, "five dollars")


class TestOrderProperties:
    """Tests for Order property setters."""
    
    def setup_method(self):
        """Reset order tracking before each test."""
        Customer._all_orders = []
        Coffee._all_orders = []
    
    def test_update_customer_valid(self):
        """Test updating an order's customer."""
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        order = Order(customer1, coffee, 2.5)
        
        order.customer = customer2
        assert order.customer == customer2
    
    def test_update_customer_invalid(self):
        """Test that updating customer to non-Customer raises TypeError."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 2.5)
        
        with pytest.raises(TypeError):
            order.customer = "Not a customer"
    
    def test_update_coffee_valid(self):
        """Test updating an order's coffee."""
        customer = Customer("Alice")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Cappuccino")
        order = Order(customer, coffee1, 2.5)
        
        order.coffee = coffee2
        assert order.coffee == coffee2
    
    def test_update_coffee_invalid(self):
        """Test that updating coffee to non-Coffee raises TypeError."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 2.5)
        
        with pytest.raises(TypeError):
            order.coffee = "Not a coffee"
    
    def test_update_price_valid(self):
        """Test updating an order's price."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 2.5)
        
        order.price = 5.0
        assert order.price == 5.0
    
    def test_update_price_invalid(self):
        """Test that updating price to invalid value raises ValueError."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 2.5)
        
        with pytest.raises(ValueError):
            order.price = 15.0


class TestOrderIntegration:
    """Integration tests for Order with Customer and Coffee."""
    
    def setup_method(self):
        """Reset order tracking before each test."""
        Customer._all_orders = []
        Coffee._all_orders = []
    
    def test_order_registered_in_customer_orders(self):
        """Test that orders are tracked in Customer._all_orders."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 2.5)
        
        assert order in customer.orders()
    
    def test_order_registered_in_coffee_orders(self):
        """Test that orders are tracked in Coffee._all_orders."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 2.5)
        
        assert order in coffee.orders()
    
    def test_multiple_orders_tracked(self):
        """Test that multiple orders are all tracked correctly."""
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Cappuccino")
        
        order1 = Order(customer1, coffee1, 2.5)
        order2 = Order(customer1, coffee2, 3.0)
        order3 = Order(customer2, coffee1, 2.0)
        
        assert len(customer1.orders()) == 2
        assert len(customer2.orders()) == 1
        assert len(coffee1.orders()) == 2
        assert len(coffee2.orders()) == 1
