with open("input.txt") as f:
    data = f.read()

print(sum(sorted(map(lambda x: sum(map(lambda y: int(y) if y else 0, x.split('\n'))), data.split('\n\n')), reverse=True)[:3]))
