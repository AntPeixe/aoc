with open("input.txt") as f:
    data = f.readlines()

obsidian = [tuple(map(int, line.split(","))) for line in data]

def get_sides(cube):
    x, y, z = cube
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]

def get_surface(cubes):
    total_sides = 6 * len(cubes)
    for cube in cubes:
        other = get_sides(cube)
        for o in other:
            if o in cubes: total_sides -= 1
    return total_sides
        
air = set()
for cube in obsidian:
    for o in get_sides(cube):
        if o not in obsidian:
            air.add(o)

# anything outside of this is for sure air and not a pocket
Xs = [o[0] for o in obsidian]
Ys = [o[1] for o in obsidian]
Zs = [o[2] for o in obsidian]
min_x, max_x = min(Xs), max(Xs)
min_y, max_y = min(Ys), max(Ys)
min_z, max_z = min(Zs), max(Zs)


def check_pocket(start, memory, visited):
    # depth first search
    # if we find something we already know then it's the same
    # if we go outside of the "obsidian box" then it's not a pocket
    # if we run out of elements in the stack then every element visited is in a pocket
    stack = [start]
    while stack:
        air_point = stack.pop(0)
        visited.add(air_point)

        result = None
        if pocket := memory.get(air_point):
            result = pocket

        if air_point[0] > max_x \
            or air_point[0] < min_x \
            or air_point[1] > max_y \
            or air_point[1] < min_y \
            or air_point[2] > max_z \
            or air_point[2] < min_z:
            result = False

        if result is not None:
            for v in visited: memory[v] = pocket
            return result

        arounds = [a for a in get_sides(air_point) if a not in obsidian and a not in visited]
        stack = arounds + stack

    for v in visited: memory[v] = True
    return True


checked_air = {}
for a in air:
    checked_air[a] = check_pocket(a, checked_air, set())

pockets = [pocket for pocket, v in checked_air.items() if v]
pocket_surface = get_surface(pockets)
obsidian_surface = get_surface(obsidian)

print(obsidian_surface - pocket_surface)
