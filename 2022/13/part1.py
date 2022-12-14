from itertools import zip_longest

with open("input.txt") as f:
    data = f.readlines()

data = [line.strip() for line in data]
data = list(filter(bool, data))

def compare_two(left, right):
    # -1 left smaller / 0 equal / 1 right smaller
    if left is None: return -1
    if right is None: return 1

    if isinstance(left, int) and isinstance(right, int):
        if left == right: return 0
        return -1 if left < right else 1

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for element_left, element_right in zip_longest(left, right):
        cmp = compare_two(element_left, element_right)
        if cmp != 0: return cmp

    # they were the same till the end
    return 0

total = 0
pair_index = 0
while data:
    pair_index += 1
    left = eval(data.pop(0))
    right = eval(data.pop(0))

    cmp = compare_two(left, right)
    if cmp == -1:
        total += pair_index

print(total)

