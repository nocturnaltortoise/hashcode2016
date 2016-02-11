from collections import Counter


class Drone:
    def __init__(self, id, max_load, init_warehouse, products_carried, is_waiting):
        self.id = id
        max_load = max_load
        self.current_load = 0
        self.warehouse = init_warehouse
        self.products = Counter(products_carried)
        self.is_waiting = is_waiting

    def load(self, products, warehouse):
        warehouse.removeProducts(products)

    def deliver(self, products, location):
        self.products.subtract(products)
        # something for indicating the order is finished

    def unload(self, products, warehouse):
        warehouse.addProducts(products)

    def wait(self, duration):
        self.is_waiting = True
        # something to handle time - drone needs to know when to stop waiting
