with open("input.txt") as f:
    data = f.readlines()

target_line = 2000000
invalid_pos = set()
beacons = set()
for line in data:
    splits = line.split()
    x = int(splits[2].replace(",", "").split("=")[1])
    y = int(splits[3].replace(":", "").split("=")[1])
    bx = int(splits[-2].replace(",", "").split("=")[1])
    by = int(splits[-1].split("=")[1])
    beacons.add((bx, by))

    dist = abs(x - bx) + abs(y - by)
    dist -= abs(y - target_line)
    invalid_pos = invalid_pos.union(set([(i, target_line) for i in range(x - dist, x + dist + 1)]))

print(len(invalid_pos - beacons))

