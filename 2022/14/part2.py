with open("input.txt") as f:
    data = f.readlines()

coordinates = [line.strip().split(" -> ") for line in data]

rocks = set()
for line in coordinates:
    coordinate_line = [tuple(map(int, coordinate.split(","))) for coordinate in line]
    rock_start = coordinate_line[0]
    for coord in coordinate_line[1:]:

        if rock_start[0] == coord[0]:
            min_h = min(rock_start[1], coord[1])
            max_h = max(rock_start[1], coord[1])
            rocks = rocks.union(set([(rock_start[0], height) for height in range(min_h, max_h + 1)]))

        if rock_start[1] == coord[1]:
            min_righ = min(rock_start[0], coord[0])
            max_righ = max(rock_start[0], coord[0])
            rocks = rocks.union(set([(right, rock_start[1]) for right in range(min_righ, max_righ + 1)]))

        rock_start = coord

rocks_floor = max([r[1] for r in rocks]) + 2
positions_in_height = [i * 2 + 1 for i in range(0, rocks_floor)]


def pos_in_triang(pos) -> bool:
    return abs(pos[0] - 500) <= positions_in_height[pos[1]] // 2


def pos_triang_edge_left(pos) -> bool:
    return 500 - pos[0] == positions_in_height[pos[1]] // 2


def pos_triang_edge_right(pos) -> bool:
    return pos[0] - 500 == positions_in_height[pos[1]] // 2


invalid_per_height = {i: set() for i in range(rocks_floor)}
[invalid_per_height[rock[1]].add(rock) for rock in rocks if pos_in_triang(rock)]

total_invalid_pos = 0
for height, positions in invalid_per_height.items():
    total_invalid_pos += len(positions)
    for pos in positions:
        if pos[1] == rocks_floor - 1:
            # no need to check below a rock on the rock floor
            continue

        if pos_triang_edge_left(pos):
            # left edge will block the left edge of next line
            below_left = (pos[0] - 1, pos[1] + 1)
            if pos_in_triang(below_left):
                invalid_per_height[height + 1].add(below_left)

        elif pos_triang_edge_right(pos):
            # right edge will block the right edge of next line
            below_right = (pos[0] + 1, pos[1] + 1)
            if pos_in_triang(below_right):
                invalid_per_height[height + 1].add(below_right)

        below = (pos[0], pos[1] + 1)
        if below in invalid_per_height[height + 1]:
            # if already invalid do not care
            continue  

        left = (pos[0] - 1, pos[1])
        right = (pos[0] + 1, pos[1])

        left_invalid = left in invalid_per_height[height] or not pos_in_triang(left)
        right_invalid = right in invalid_per_height[height] or not pos_in_triang(right)

        if left_invalid and right_invalid:
            invalid_per_height[height + 1].add(below)

print(sum(positions_in_height) - total_invalid_pos)

