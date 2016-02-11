from Warehouse import Warehouse
from Order import Order
from Product import Product


def convert_coord(string):
    return tuple([int(line) for line in string.split(' ')])

def convert_products(string, weights):
    products = string.split(' ')
    con_products = []
    for product_no in range(len(products)):
        product = products[product_no]

        if product != '0':
            con_products.append(Product(product_no, weights[product_no]))

    return con_products


def parse(file):
    file = open(file)
    lines = [line.rstrip('\r\n') for line in file.readlines()]

    variables = lines[0].split(' ')
    r, c, drones, deadline, max_load = variables

    products_count = int(lines[1])

    products = [Product(index, int(lines[2].split(' ')[index])) for index in range(len(lines[2].split(' ')))]

    warehouse_count = int(lines[3])

    warehouses = [Warehouse(convert_coord(lines[warehouse_no+4]), convert_products(lines[warehouse_no+5], products), warehouse_no) for warehouse_no in range(warehouse_count*2-1)]


    orders_offset = 4 + warehouse_count * 2

    orders_count = int(lines[orders_offset])

    orders = [Order(convert_coord(lines[order_no + orders_offset]), lines[order_no + orders_offset+2], order_no) for order_no in range(orders_count*3-1)]

    return {
        'orders': orders,
        'warehouses': warehouses
    }

data = parse('data/busy_day.in')

# for product in list(data['warehouses'][0].products.elements()):
#     print(str(product))
#
# for order in data['orders']:
#     for product in list(order.products.elements()):
#         print(str(product))