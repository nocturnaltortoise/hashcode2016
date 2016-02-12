import parser
from Drone import Drone

parsed_file = parser.parse('data/busy_day.in')
drone_count = parsed_file['variables'][2]
max_load = parsed_file['variables'][4]
init_warehouse = parsed_file['warehouses'][0]
drones = []
for i in range(int(drone_count)):
    drones.append(Drone(i, max_load, init_warehouse, [], False))

orders = parsed_file['orders']
warehouses = parsed_file['warehouses']

world_state = (drones, orders, warehouses)

def evaluate(dna):

    commands = dna.split('|')

    # (T − t) / T × 100
    total = len(commands)

    time = 0
    total_score = 0

    for command in commands:
        drone, action, product, warehouse, amount = command

        if action == 'D':
            total_score += (total - time) / total * 100

        time += 1

    return total_score


print(evaluate('0L001|0D101'))