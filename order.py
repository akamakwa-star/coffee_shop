from customer import Customer
from coffee import Coffee


class Order:
    """Represents an order placed at the coffee shop."""
    
    def __init__(self, customer, coffee, price):
        """
        Initialize an Order with customer, coffee, and price.
        
        Args:
            customer (Customer): The customer placing the order
            coffee (Coffee): The coffee being ordered
            price (float): The price of the order (must be 1.0-10.0)
            
        Raises:
            TypeError: If customer is not a Customer or coffee is not a Coffee
            ValueError: If price is invalid
        """
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        # Register order in both Customer and Coffee tracking lists
        Customer._all_orders.append(self)
        Coffee._all_orders.append(self)
    
    @property
    def customer(self):
        """Get the customer for this order."""
        return self._customer
    
    @customer.setter
    def customer(self, value):
        """
        Set the customer for this order with validation.
        
        Args:
            value (Customer): The customer instance
            
        Raises:
            TypeError: If value is not a Customer instance
        """
        if not isinstance(value, Customer):
            raise TypeError("Customer must be a Customer instance.")
        self._customer = value
    
    @property
    def coffee(self):
        """Get the coffee for this order."""
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        """
        Set the coffee for this order with validation.
        
        Args:
            value (Coffee): The coffee instance
            
        Raises:
            TypeError: If value is not a Coffee instance
        """
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be a Coffee instance.")
        self._coffee = value
    
    @property
    def price(self):
        """Get the price of this order."""
        return self._price
    
    @price.setter
    def price(self, value):
        """
        Set the price of this order with validation.
        
        Args:
            value (float): The price (must be between 1.0 and 10.0)
            
        Raises:
            TypeError: If price is not a number
            ValueError: If price is not between 1.0 and 10.0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if value < 1.0 or value > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = value
