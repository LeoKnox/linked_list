from store_one import *
from store_two import *

coke = Product("Coke", "1", "beverage")
coke.print_info()
coke.update_price(50, False)
coke.print_info()
seven_twelve = Store("7/12")
seven_twelve.add_product("Biscuit", "2", "foood")
seven_twelve.add_product("Motor Oil", "4", "automotive")
seven_twelve.inflation(10)
print(seven_twelve.product_list[0].print_info())
seven_twelve.sell_product(0)
seven_twelve.set_clearance("automotive", 15)
print(seven_twelve.product_list[0].print_info())


