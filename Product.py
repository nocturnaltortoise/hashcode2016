class Product:
    def __init__(self, type_id, weight):
        self.type_id = type_id
        self.weight = weight

    def __str__(self):
        return str(self.type_id)

    def __eq__(self, other):
        return self.type_id == other.type_id and self.weight == other.weight

    def __attrs(self):
        return self.type_id, self.weight

    def __hash__(self):
        return hash(self.__attrs())