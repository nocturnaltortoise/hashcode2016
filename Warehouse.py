from collections import Counter


class Warehouse:
    def __init__(self, location, products, id):
        self.location = location
        self.products = Counter(products)
        self.id = id

    def removeProducts(self, products):
        self.products.subtract(products)

    def addProducts(self, products):
        self.products.update(products)