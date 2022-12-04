with open("input.txt") as f:
    data = f.readlines()

data = list(map(str.strip, data))
data = [[int(i) for i in line] for line in data]

n_rows = len(data)
n_cols = len(data[0])

lowest_points = []
for i in range(n_rows):
    for j in range(n_cols):
        curr = data[i][j]
        if i > 0 and data[i-1][j] <= curr:
            continue
        if i < n_rows - 1 and data[i+1][j] <= curr:
            continue
        if j > 0 and data[i][j-1] <= curr:
            continue
        if j < n_cols - 1 and data[i][j+1] <= curr:
            continue
        lowest_points.append(curr)


print(lowest_points)
print(sum(lowest_points) + len(lowest_points))
