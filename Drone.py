class Drone:
    def __init__(self, max_load, init_warehouse, products_carried):
        max_load = max_load
        self.current_load = 0
        self.warehouse = init_warehouse
        self.products = products_carried

    def load(self, products, warehouse):
        pass

    def deliver(self, products, location):
        pass

    def unload(self, products, warehouse):
        pass

    def wait(self, duration):
        pass
