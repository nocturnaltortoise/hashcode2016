from collections import Counter
from OrderWriter import OrderWriter
from Warehouse import Warehouse


class Drone:
    def __init__(self, id, max_load, init_warehouse, products_carried, is_waiting):
        self.id = id
        max_load = max_load
        self.current_load = 0
        self.warehouse = init_warehouse
        self.products = Counter(products_carried)
        self.is_waiting = is_waiting

    def load(self, products, warehouse):
        counted_products = Counter(products)
        if not(self.warehouse == warehouse):
            self.move(warehouse)

        warehouse.removeProducts(counted_products)
        OrderWriter.write([self.id, "L", warehouse.id, OrderWriter.products_to_string(counted_products)])

    def deliver(self, order, products, location):
        counted_products = Counter(products)
        self.products.subtract(products)
        # something for indicating the order is finished

        OrderWriter.write([self.id, "D", order.id, OrderWriter.products_to_string(counted_products)])

    def unload(self, products, warehouse):
        counted_products = Counter(products)
        if not(self.warehouse == warehouse):
            self.move(warehouse)

        warehouse.addProducts(counted_products)
        OrderWriter.write([self.id, "U", warehouse.id, OrderWriter.products_to_string(counted_products)])

    def move(self, warehouse):
        self.warehouse = warehouse

    def wait(self, duration):
        self.is_waiting = True
        # something to handle time - drone needs to know when to stop waiting

        OrderWriter.write([self.id, "W", duration])

# w = Warehouse((452, 341), [23, 34, 46], 10)
#
# d = Drone(0, 200, 0, [23, 34, 46], False)
# d.load([45, 45], w)