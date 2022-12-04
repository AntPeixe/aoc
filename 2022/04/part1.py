with open("input.txt") as f:
    data = f.readlines()

data = [pair.strip().split(',') for pair in data]
all_split = list(map(lambda pairs: (list(map(int, pairs[0].split('-'))), list(map(int, pairs[1].split('-')))), data))

def is_contained(a, b):
    return a[0] <= b[0] and a[1] >= b[1]
print(sum([is_contained(first, second) or is_contained(second, first) for first, second in all_split]))

