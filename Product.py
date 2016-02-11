class Product:
    def __init__(self, type_id, weight):
        self.type_id = type_id
        self.weight = weight

    def __str__(self):
        return self.type_id