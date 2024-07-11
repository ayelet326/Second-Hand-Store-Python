class Product:
    """Product class represents a product in the store."""

    def __init__(self, name, count, cost):
        self.name = name
        self.count = count
        self.cost = cost

    def print_product(self):
        """print this product"""
        print(f"Name:{self.name}\nUnits in Stock{self.count}\nPrice:{self.cost}\n ")
