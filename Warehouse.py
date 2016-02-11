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

    def __attrs(self):
        return (self.location, self.products, self.id)

    def __hash__(self):
        return hash(self.__attrs())

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return str(self.id)