
class Customer:
    """Represents a coffee shop customer."""
    
    # Class variable to store all orders across all customers
    _all_orders = []
    
    def __init__(self, name):
        """
        Initialize a Customer with a name.
        
        Args:
            name (str): Customer's name (must be 1-15 characters)
            
        Raises:
            ValueError: If name is invalid
            TypeError: If name is not a string
        """
        self.name = name
    
    @property
    def name(self):
        """Get the customer's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Set the customer's name with validation.
        
        Args:
            value (str): Customer's name (must be 1-15 characters)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name length is not between 1-15 characters
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters long.")
        self._name = value
    
    def orders(self):
        """
        Get all orders placed by this customer.
        
        Returns:
            list: List of Order instances for this customer
        """
        return [order for order in self._all_orders if order.customer == self]
    
    def coffees(self):
        """
        Get unique coffees ordered by this customer.
        
        Returns:
            list: Unique list of Coffee instances ordered by this customer
        """
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        """
        Create a new order for this customer.
        
        Args:
            coffee (Coffee): The coffee to order
            price (float): The price of the order (1.0-10.0)
            
        Returns:
            Order: The newly created Order instance
        """
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order
    
    @classmethod
    def most_aficionado(cls, coffee):
        """
        Find the customer who has spent the most money on a given coffee.
        
        Args:
            coffee (Coffee): The coffee to check
            
        Returns:
            Customer: The customer with highest spending on this coffee, or None
        """
        coffee_orders = [order for order in cls._all_orders if order.coffee == coffee]
        
        if not coffee_orders:
            return None
        
        # Group orders by customer and calculate total spending
        customer_spending = {}
        for order in coffee_orders:
            if order.customer not in customer_spending:
                customer_spending[order.customer] = 0
            customer_spending[order.customer] += order.price
        
        # Return the customer with the highest spending
        return max(customer_spending, key=customer_spending.get)
