from store_two import *

class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []
    def add_product(self, name, price, category):
        self.product_list.append(Product(name, price, category))
    def sell_product(self, id):
        self.product_list.pop(id);
    def inflation(self, percent_increase):
        for item in range (len(self.product_list)):
            self.product_list[item].update_price(percent_increase, True)
    def set_clearance(self, category, percent_discount):
        for item in range (len(self.product_list)):
            if (self.product_list[item].category==category):
                self.product_list[item].update_price(percent_discount, False)

