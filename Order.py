from collections import Counter


class Order:
    def __init__(self, products, delivery_location, id):
        self.delivery_location = delivery_location
        self.products = Counter(products)
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

    def __attrs(self):
        return (self.delivery_location, self.products, self.id)

    def __hash__(self):
        return hash(self.__attrs())