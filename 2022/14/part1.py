from typing import Tuple, Optional


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

sand_units = set()

def get_top_sand_or_rock_in_col(x: int, y: int) -> Optional[Tuple[int, int]]:
    same_col = [r for r in rocks if r[0] == x] + [s for s in sand_units if s[0] == x]
    same_col = [k for k in same_col if k[1] > y]
    if same_col:
        top = same_col[0]
        for k in same_col:
            top = top if top[1] < k[1] else k
        return top
    return None


done = False
while not done:
    pour_x = 500
    pour_y = 0

    while True:
        floor = get_top_sand_or_rock_in_col(pour_x, pour_y)
        if floor is None:
            done = True
            break

        elif (floor[0] - 1, floor[1]) not in rocks.union(sand_units):
            pour_x = floor[0] - 1
            pour_y = floor[1]
    
        elif (floor[0] + 1, floor[1]) not in rocks.union(sand_units):
            pour_x = floor[0] + 1
            pour_y = floor[1]

        else: # should stay on top of this "floor"
            sand_units.add((floor[0], floor[1] - 1))
            break

print(len(sand_units))

