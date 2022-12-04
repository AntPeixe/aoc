with open("input.txt") as f:
    data = f.readlines()

data = list(map(str.strip, data))
data = [[int(i) for i in line] for line in data]

n_rows = len(data)
n_cols = len(data[0])

basins = {}
used_pos = set()

basin_count = 0
for i in range(n_rows):
    for j in range(n_cols):
        if data[i][j] == 9: continue
        if (i,j) in used_pos: continue
        
        pos = [(i,j)]
        rolling_basin = set()
        while pos:
            i, j = pos.pop(0)
            if data[i][j] == 9: continue
            if (i,j) in rolling_basin: continue
            rolling_basin.add((i,j))

            new_pos = []
            if i > 0: new_pos.append((i-1, j))
            if j > 0: new_pos.append((i, j-1))
            if i < n_rows - 1: new_pos.append((i+1, j))
            if j < n_cols - 1: new_pos.append((i, j+1))

            pos = pos + new_pos

        if rolling_basin:
            basins[basin_count] = rolling_basin
            basin_count += 1
            used_pos = used_pos.union(rolling_basin)

biggest_basins = sorted([len(v) for v in basins.values()])[-3:]
total = 1
for bb in biggest_basins:
    total *= bb
print(total)
