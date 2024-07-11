from Product import Product
from second_hand_product import SecondHandProduct


class Shop:
    """This class represents a store """

    def __init__(self, name, current_profits):
        self.name = name
        self.dic_product = {"miri": {"count": 6, "cost": 100}}
        self.dic_second_hand_product = {"i": {"count": 6, "cost": 100, "levelYad": 2, "needFix": True},
                                        "y": {"count": 1, "cost": 100, "levelYad": 3, "needFix": True}}
        self.profits = current_profits
        self.Product_Catalog = open("product_catalog.txt", 'r')

    def find_product(self, product):
        """this function get product and search the product in dictionary,if found return true, else False"""
        for k in self.dic_product.keys():
            if k == product.name:
                return True
        return False

    def find_second_hand_product(self, Y2pr):
        """this function get product and search the product in dictionary,if found return true, else False"""
        for k, v in self.dic_second_hand_product.items():
            if k == Y2pr.name:
                if Y2pr.needFix == v['needFix']:
                    if v['hand_level'] == Y2pr.hand_level:
                        return True
        return False

    def add_second_hand_product(self):
        """This function adds a second-hand product to the second-hand dictionary"""
        name = input("Name of the product? (enter string): ")

        while True:
            count = input("Number of products? (enter num): ")
            try:
                count = int(count)
                break
            except ValueError:
                print("The count is not valid, please enter a number.")

        while True:
            cost = input("Price of the product? (enter num): ")
            try:
                cost = int(cost)
                break
            except ValueError:
                print("The cost is not valid, please enter a number.")

        while True:
            level = input("Which hand level? (enter num): ")
            try:
                level = int(level)
                break
            except ValueError:
                print("The level is not valid, please enter a number.")

        needFix = input("Need fix? (T/F): ").strip().lower()
        needFix = True if needFix == 't' else False

        Y2p = SecondHandProduct(name, count, cost, level, needFix)

        if not self.find_second_hand_product(Y2p):
            Y2p.add_product_to_catalog()
            self.dic_second_hand_product[Y2p.name] = {"count": Y2p.count, "cost": Y2p.cost,
                                                      "hand_level": Y2p.hand_level, "needFix": Y2p.needFix}
        else:
            for k, v in self.dic_second_hand_product.items():
                if k == Y2p.name:
                    if Y2p.needFix == v['needFix'] and Y2p.hand_level == v['hand_level']:
                        self.dic_second_hand_product[k]['count'] += Y2p.count
        print("The product was added successfully.👌")

    def print_catalog(self):
        """A function that will print all the products in the store from a catalog file"""
        [print(f"{line}") for line in list(self.Product_Catalog.readlines())]
        self.Product_Catalog.seek(0)

    def payment_management(self, cost):
        """The function receives a product price and collects a payment from the user until the payment is
        appropriate returns true when paid otherwise false"""
        pay = int(input("💰 enter your pay"))
        print(cost + pay)
        print(pay)
        print((pay - cost) > 0)
        if (pay - cost) > 0:
            print("in if")
            self.profits += pay
            return True
        else:

            while (pay < cost) & (pay != -1):
                pay = int(input("💰 the pay not enough,enter again ,to cancel press-1"))
            if pay == -1:
                return False
        self.profits += pay
        return True

    update_count = lambda self, count, c_down: count - c_down

    def buy(self):
        """this function manager buy"""
        product_choose = input("write name of product that you want to buy")
        kind = input("New or second hand product?(s/n)")
        if kind == "n":
            count = input("some products?")
            price = input("some price?")
            try:
                price = int(price)
            except:
                print("thr price not valid❗❗❗")
                return False
            product = Product(product_choose, count, price)
            if not self.find_second_hand_product(product):
                print("the product is not exists 😔😕😕")
                return False
            elif self.dic_product[product_choose]['count'] < product.count:
                print("out of stock")
                return False
            else:
                if not self.payment_management(product.cost):
                    return False
                else:
                    self.update_count(self.dic_product[product_choose]['count'], product.count)
                    print("The purchase was made successfully!👌\nProduct information:")
                    product.print_product()
                    return True
        elif kind == "s":

            count = input("some products?")
            try:
                count = int(count)
            except:
                print("thr count not valid❗❗❗")
                return False
            price = input("some price?")
            try:
                price = int(price)
            except:
                print("thr price not valid❗❗❗")
                return False
            level = input("Which level yad?")
            try:
                level = int(level)
            except:
                print("thr level not valid❗❗❗")
                return False
            needFix = input("Need fix? (True/False) ").strip().lower()
            needFix = True if needFix == "t" else False

            product1 = SecondHandProduct(product_choose, count, price, level, needFix)
            if not self.find_second_hand_product(product1):
                print("the product is not exists")
                return False
            elif self.dic_second_hand_product[product_choose]['count'] < product1.count:
                print("out of stock")
                return False
            else:
                if not self.payment_management(product1.cost):
                    return False
                else:
                    self.update_count(self.dic_second_hand_product[product_choose]['count'], product1.count)
                    print("The purchase was made successfully!👌"
                          "\n📑 Product information:")
                    product1.print_product()
                    return True
