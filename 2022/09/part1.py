with open("input.txt") as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

h_pos = (0, 0)
t_pos = (0, 0)

visited_pos = set([t_pos])
for direction, amount in map(lambda x: x.split(), data):
    amount = int(amount)
    new_positions = set()

    if direction == "R":
        h_pos = (h_pos[0] + amount, h_pos[1])
        row = t_pos[1] if t_pos[1] == h_pos[1] else h_pos[1]
        if abs(h_pos[0] - t_pos[0]) > 1:
            new_positions = set([(r, row) for r in range(t_pos[0] + 1, h_pos[0])])
            t_pos = (h_pos[0] - 1, row)

    if direction == "U":
        h_pos = (h_pos[0], h_pos[1] + amount)
        col = t_pos[0] if t_pos[0] == h_pos[0] else h_pos[0]
        if abs(h_pos[1] - t_pos[1]) > 1:
            new_positions = set([(col, r) for r in range(t_pos[1] + 1, h_pos[1])])
            t_pos = (col, h_pos[1] - 1)

    if direction == "L":
        h_pos = (h_pos[0] - amount, h_pos[1])
        row = t_pos[1] if t_pos[1] == h_pos[1] else h_pos[1]
        if abs(h_pos[0] - t_pos[0]) > 1:
            new_positions = set([(r, row) for r in range(t_pos[0] - 1, h_pos[0], -1)])
            t_pos = (h_pos[0] + 1, row)

    if direction == "D":
        h_pos = (h_pos[0], h_pos[1] - amount)
        col = t_pos[0] if t_pos[0] == h_pos[0] else h_pos[0]
        if abs(h_pos[1] - t_pos[1]) > 1:
            new_positions = set([(col, r) for r in range(t_pos[1] - 1, h_pos[1], -1)])
            t_pos = (col, h_pos[1] + 1)

    visited_pos = visited_pos.union(new_positions)

print(len(visited_pos))

