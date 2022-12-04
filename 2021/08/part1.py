with open("input.txt") as f:
    data = f.readlines()

codes = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
n_seg = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

data = [line.strip().split(' | ') for line in data]
unique_nums = 0
for line in data:
    for n in line[1].split():
        if len(set(n)) in {2, 4, 3, 7}:
            unique_nums += 1

print(unique_nums)
