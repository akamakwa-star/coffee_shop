
class Coffee:
    """Represents a coffee product."""
    
    # Class variable to store all orders across all coffees
    _all_orders = []
    
    def __init__(self, name):
        """
        Initialize a Coffee with a name.
        
        Args:
            name (str): Coffee's name (must be at least 3 characters)
            
        Raises:
            ValueError: If name is invalid
            TypeError: If name is not a string
        """
        self.name = name
    
    @property
    def name(self):
        """Get the coffee's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Set the coffee's name with validation.
        
        Args:
            value (str): Coffee's name (must be at least 3 characters)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name length is less than 3 characters
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = value
    
    def orders(self):
        """
        Get all orders for this coffee.
        
        Returns:
            list: List of Order instances for this coffee
        """
        return [order for order in self._all_orders if order.coffee == self]
    
    def customers(self):
        """
        Get unique customers who have ordered this coffee.
        
        Returns:
            list: Unique list of Customer instances who ordered this coffee
        """
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        """
        Get the total number of times this coffee has been ordered.
        
        Returns:
            int: Total number of orders for this coffee
        """
        return len(self.orders())
    
    def average_price(self):
        """
        Get the average price at which this coffee has been ordered.
        
        Returns:
            float: Average price of orders for this coffee, or 0 if no orders
        """
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)
