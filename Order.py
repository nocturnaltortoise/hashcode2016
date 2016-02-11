from collections import Counter


class Order:
    def __init__(self, products, delivery_location, id, is_finished):
        self.delivery_location = delivery_location
        self.products = Counter(products)
        self.id = id
        self.is_finished = is_finished