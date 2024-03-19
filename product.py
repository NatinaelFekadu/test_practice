class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotal(self):
        if self.price < 0 or self.quantity < 0:
            raise ValueError("Negative values are not allowed")
        return self.price * self.quantity
