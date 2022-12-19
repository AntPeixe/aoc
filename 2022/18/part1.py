with open("input.txt") as f:
    data = f.readlines()

obsidian = [tuple(map(int, line.split(","))) for line in data]

total_sides = 6 * len(obsidian)
for cube in obsidian:
    x, y, z = cube
     
    other = [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]
    for o in other:
        if o in obsidian: total_sides -= 1
        
print(total_sides)
