import numpy as np

# input_file = "day6_test.txt"
input_file = "day6.txt"

with open(input_file) as f:
    data = f.readline()
    data = list(map(int, data.split(",")))


"""
fishes = np.array(data)
for _ in range(256):
    fishes = fishes - 1
    new_fish_count = (fishes == -1).sum()
    fishes[fishes == -1] = 6
    new_fishes = np.ones(new_fish_count) * 8
    fishes = np.concatenate([fishes,new_fishes])
print(fishes.shape)
"""

fishes = {i: 0 for i in range(9)}
for i in data:
    fishes[i] += 1

print(fishes)

for k in range(256):
    new_fishes = fishes[0]
    for i in range(1,9):
        fishes[i-1] = fishes[i]
    fishes[8] = new_fishes
    fishes[6] += new_fishes

print(sum(list(fishes.values())))
