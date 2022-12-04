import numpy as np

# input_file = "day5_test.txt"
input_file = "day5.txt"

with open(input_file) as f:
    data = f.readlines()

data = [l.strip().split(" -> ") for l in data]
data = [[tuple(map(int, point.split(","))) for point in l] for l in data]


def is_horizontal(line):
    a, b = line
    return a[0] == b[0]


def is_vertical(line):
    a, b = line
    return a[1] == b[1]

def is_diag(line):
    a, b = line
    return abs(a[0] - b[0]) == abs(a[1] - b[1])


max_dim = max([max(max(l[0]), max(l[1])) for l in data]) + 1

matrix = np.zeros((max_dim, max_dim))
for line in data:
    if is_horizontal(line):
        x = line[0][0]
        y_min = min(line[0][1], line[1][1])
        y_max = max(line[0][1], line[1][1])
        for i in range(y_min, y_max+1):
            matrix[x][i] += 1

    if is_vertical(line):
        y = line[0][1]
        x_min = min(line[0][0], line[1][0])
        x_max = max(line[0][0], line[1][0])
        for i in range(x_min, x_max+1):
            matrix[i][y] += 1

    if is_diag(line):
        if line[1][0] < line[0][0]:
            x = range(line[0][0],line[1][0]-1, -1)
        else:
            x = range(line[0][0],line[1][0]+1)
        if line[1][1] < line[0][1]:
            y = range(line[0][1],line[1][1]-1, -1)
        else:
            y = range(line[0][1],line[1][1]+1)

        for i,j in zip(x,y):
            matrix[i][j] += 1

print(matrix)
print((matrix > 1).sum())
