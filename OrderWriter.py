from collections import Counter


class OrderWriter:
    @staticmethod
    def write(order_list):
        with open("output.txt", "a") as f:
            for item in order_list:
                f.write(str(item) + " ")
            f.write("\n")

    @staticmethod
    def products_to_string(product_counter):
        for product in product_counter:
            print(product_counter[product])
            product_string = str(product.type_id) + " " + str(product_counter[product])

        return product_string

