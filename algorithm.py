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