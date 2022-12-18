with open("input.txt") as f:
    data = f.readlines()

max_coord = 4000000

sensors = []
outside_points = set()

for line in data:
    splits = line.split()
    x = int(splits[2].replace(",", "").split("=")[1])
    y = int(splits[3].replace(":", "").split("=")[1])
    bx = int(splits[-2].replace(",", "").split("=")[1])
    by = int(splits[-1].split("=")[1])
    
    dist = abs(x - bx) + abs(y - by)

    sensors.append((x, y, dist))
    
    outside_dist = dist + 1
    for i in range(outside_dist + 1):
        outside_points.add((x + outside_dist - i, y + i))
        outside_points.add((x + outside_dist - i, y - i))
        outside_points.add((x - outside_dist + i, y + i))
        outside_points.add((x - outside_dist + i, y - i))

outside_points = filter(lambda p: 0 <= p[0] <= max_coord and 0 <= p[1] <= max_coord, outside_points)
for p in outside_points:
    if all([abs(p[0] - bx) + abs(p[1] - by) > dist for bx, by, dist in sensors]):
        print(p[0] * 4000000 + p[1])
        break

