from Product import Product


class SecondHandProduct(Product):
    """This class represents a product in a second-hand store."""
    def __init__(self, name, count, cost, hand_level, needFix):
        super().__init__(name, count, cost)
        self.hand_level = hand_level
        self.needFix = needFix

    def print_product(self):
        """print this product"""
        print(f"Name:{self.name}\n"
              f"Units in Stock : {self.count}\n"
              f"Price:{self.cost}\n"
              f"Yad number:{self.hand_level}\n"
              f"Needed repair:{self.needFix}\n")

    def add_product_to_catalog(self):
        """add product to catalog"""
        Product_Catalog = open("product_catalog.txt",'a')
        Product_Catalog.write(f"\nName :{self.name},Cost: {self.cost},levelYad:{self.hand_level}, needFix:{self.needFix}")
        Product_Catalog.seek(0)
