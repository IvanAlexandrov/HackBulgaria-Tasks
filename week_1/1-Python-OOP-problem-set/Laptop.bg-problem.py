class Product(object):
    """Base Class"""

    def __init__(self,  name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    '''Inherit Base Class'''

    def __init__(self, name, stock_price, final_price, disk_space, ram_memory):
        super().__init__(name, stock_price, final_price)
        self.disk_space = disk_space
        self.ram_memory = ram_memory


class Smartphone(Product):
    '''Inherit Base Class'''

    def __init__(self, name, stock_price, final_price, display, megapixels):
        super().__init__(name, stock_price, final_price)
        self.display = display
        self.megapixels = megapixels


class Store(object):

    def __init__(self, name):
        self.name = name
        self.products = {}
        self.total = 0

    def load_new_products(self, product, count):
        if product.name not in self.products:
            self.products[product] = count
        else:
            self.products[product] += count

    def list_products(self, product_class):
        list_of_products = ''
        for product in self.products:
            if isinstance(product, product_class):
                list_of_products += product.name + " - " + str(self.products[product]) + "\n"
        return list_of_products

    def sell_product(self, product):
        if product in self.products:
            if self.products[product] > 0:
                self.products[product] -= 1
                self.total += product.profit()
            else:
                return False

    def total_income(self, product):
        return self.total

new_product = Product('HP HackBook', 1000, 1243)
laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
new_store = Store('Laptop.bg')
new_store.load_new_products(smartphone, 20)
new_store.load_new_products(laptop, 10)
print(new_store.list_products(Laptop))
new_store.sell_product(laptop)
print(new_store.list_products(Laptop))
print(new_store.total_income(laptop))
"""
store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store.load_new_products(smarthphone, 2)
store.sell_product(smarthphone) # True
store.sell_product(smarthphone) # True

store.total_income() # 640
"""
