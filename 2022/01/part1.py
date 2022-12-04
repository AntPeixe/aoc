with open("input.txt") as f:
    data = f.read()

print(max(map(lambda x: sum(map(lambda y: int(y) if y else 0, x.split('\n'))), data.split('\n\n'))))
