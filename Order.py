from collections import Counter


class Order:
    def __init__(self, products, delivery_location):
        self.delivery_location = delivery_location
        self.products = Counter(products)