import math

with open("input.txt") as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

def move_towards_by_one(start, target):
    if abs(target[0] - start[0]) <= 1 and abs(target[1] - start[1]) <= 1:
        # target around start
        return start

    if abs(target[0] - start[0]) > 1 and abs(target[1] - start[1]) > 1:
        # target two away diagonally
        return math.ceil((target[0] + start[0]) / 2), math.ceil((target[1] + start[1]) / 2)

    if abs(target[1] - start[1]) > 1:
        return target[0], math.ceil((target[1] + start[1]) / 2)
        
    if abs(target[0] - start[0]) > 1:
        return math.ceil((target[0] + start[0]) / 2), target[1]


h_pos = (0, 0)
tails_pos = [(0, 0) for _ in range(9)]
visited_pos = [(0,0)]

for direction, amount in map(lambda x: x.split(), data):
    for _ in range(int(amount)):
        if direction == "R":
            h_pos = (h_pos[0] + 1, h_pos[1])

        elif direction == "U":
            h_pos = (h_pos[0], h_pos[1] + 1)

        elif direction == "L":
            h_pos = (h_pos[0] - 1, h_pos[1])

        elif direction == "D":
            h_pos = (h_pos[0], h_pos[1] - 1)

        tails_pos[0] = move_towards_by_one(tails_pos[0], h_pos)

        for idx in range(1, len(tails_pos)):
            tails_pos[idx] = move_towards_by_one(tails_pos[idx], tails_pos[idx - 1])
            if idx == 8:
                visited_pos.append(tails_pos[idx])

print(len(visited_pos))

