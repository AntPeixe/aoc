from typing import Dict, Generator, Tuple


with open("input.txt") as f:
    data = f.readlines()

valves = {}
for line in data:
    line = line.split()
    valve = line[1]
    rate = int(line[4].split("=")[1].replace(";", ""))
    next_valves = list(map(lambda x: x.replace(",", ""), line[9:]))
    valves[valve] = (rate, next_valves)
    
def breadth_first(start, end=None):
    stack = [[start]]
    visited = set()
    dist = 0
    cost = {}
    while stack:
        nodes: list = stack.pop() 
        next_level_node = set()
        for node in nodes:
            if end and node == end:
                return dist
            visited.add(node)
            cost[node] = dist
            next_level_node = next_level_node.union(set(valves[node][1]))
        
        next_level_node = [n for n in next_level_node if n not in visited]
        if next_level_node:
            stack = [list(next_level_node)] + stack
        dist += 1
    return cost

# valve, time, open valves, current rate, released
stack = [("AA", 0, set(), 0, 0)]
max_released = stack[0]
paths = 0
while stack:
    popped = stack.pop(0)
    paths += 1
    current_v, current_time, current_open, current_rate, current_released = popped
    
    if (30 - current_time) * current_rate + current_released > (30 - max_released[1]) * max_released[-2] + max_released[-1]:
        max_released = popped

    if current_time >= 30:
        continue

    distances = breadth_first(current_v)

    for v, (rate, _) in valves.items():
        if rate == 0: continue
        if v in current_open: continue
        
        time_to_skip = min(30 - current_time, distances[v] + 1)
        new_released =  time_to_skip * current_rate + current_released
        new_rate = current_rate + valves[v][0]
        new_time = current_time + time_to_skip
        new_open = current_open.copy()
        new_open.add(v)
        stack.append((v, new_time, new_open, new_rate, new_released))
        
total_released = (30 - max_released[1]) * max_released[-2] + max_released[-1]
print(total_released)

