class OrderWriter:
    @staticmethod
    def write(order_list):
        with open("output.txt", "a") as f:
            for item in order_list:
                f.write(str(item))
            f.write("\n")

OrderWriter.write([0,"W",3])