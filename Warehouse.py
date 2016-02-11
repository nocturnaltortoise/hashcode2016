from collections import Counter

class Warehouse:
    def __init__(self, location, products):
        self.location = location
        self.products = Counter(products)

    def removeProduct(self, products):
        self.products.subtract(products)

    def addProduct(self, products):
        self.products.update(products)