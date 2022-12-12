with open("input.txt") as f:
    data = f.readlines()

start = None
end = None
grid = []
for i, line in enumerate(data):
    row = []
    for j, position in enumerate(line):
        if position == "S":
            row.append(ord("a"))
            start = (i, j)
        elif position == "E":
            row.append(ord("z"))
            end = (i,j)
        else:
            row.append(ord(position))
    grid.append(row)


def get_directions(node: tuple) -> list:
    directions = [
        (node[0] - 1, node[1]),  # up
        (node[0], node[1] - 1),  # left
        (node[0] + 1, node[1]),  # down
        (node[0], node[1] + 1),  # right
    ]

    return [d for d in directions if d[0] >= 0 and d[0] < len(grid) and d[1] >= 0 and d[1] < len(grid[0])]

similar_nodes = set()
nodes_to_check = [start]
start_height = grid[start[0]][start[1]]
while nodes_to_check:
    node = nodes_to_check.pop()
    if node in similar_nodes: continue

    similar_nodes.add(node)
    directions = get_directions(node)
    directions = [d for d in directions if d not in similar_nodes]
    directions = [d for d in directions if grid[d[0]][d[1]] == start_height]

    nodes_to_check = directions + nodes_to_check


steps = []
for starting_node in similar_nodes:
    visited = set()
    stack = [[starting_node]]
    levels_visited = 0
    while end not in visited:
        nodes: list = stack.pop()
        next_level_node = set()
        for node in nodes:
            visited.add(node)
            node_height = grid[node[0]][node[1]]
            directions = get_directions(node)

            # filter already visited
            directions = [d for d in directions if d not in visited]
            # filter positions too high
            directions = [d for d in directions if grid[d[0]][d[1]] <= node_height + 1]

            next_level_node = next_level_node.union(set(directions))
        
        stack = [list(next_level_node)] + stack
        levels_visited += 1

    steps.append(levels_visited - 1)

print(min(steps))

