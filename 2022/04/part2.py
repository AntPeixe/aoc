with open("input.txt") as f:
    data = f.readlines()

data = [pair.strip().split(',') for pair in data]
all_split = list(map(lambda pairs: (list(map(int, pairs[0].split('-'))), list(map(int, pairs[1].split('-')))), data))

def has_overlap(a, b):
    return a[0] <= b[1] and a[1] >= b[0]
print(sum([has_overlap(first, second) for first, second in all_split]))
