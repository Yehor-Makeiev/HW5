def formatted_numbers():
    result = []
    result.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))
    for i in range(16):
        result.append("|{:<10d}|{:^10x}|{:>10b}|".format(i, i, i))
    return result


for el in formatted_numbers():
    print(el)