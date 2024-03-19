class Product:
    def __init__(self, name, price, quantity):
        """
        Initialize the object with the provided name, price, and quantity.

        Parameters:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item.

        Returns:
            None
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotal(self):
        """
        Calculate the total by multiplying the price with the quantity.

        No parameters.
        
        Returns:
            float: The total calculated by multiplying price and quantity.
        """
        if self.price < 0 or self.quantity < 0:
            raise ValueError("Negative values are not allowed")
        return self.price * self.quantity
