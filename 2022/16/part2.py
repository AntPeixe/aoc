"""
Disclaimer: The approach used was not originally thought by me. I tried to do both agents at the same time but the
search space was too large and no attempt of optimization was making it better.

After trying a lot of different things I read about the approach of running one after another.
"""

with open("input.txt") as f:
    data = f.readlines()

valves = {}
for line in data:
    line = line.split()
    valve = line[1]
    rate = int(line[4].split("=")[1].replace(";", ""))
    next_valves = list(map(lambda x: x.replace(",", ""), line[9:]))
    valves[valve] = (rate, next_valves)
    
def get_costs(start):
    stack = [[start]]
    visited = set()
    dist = 0
    cost = {}
    while stack:
        nodes: list = stack.pop() 
        next_level_node = set()
        for node in nodes:
            visited.add(node)
            cost[node] = dist
            next_level_node = next_level_node.union(set(valves[node][1]))
        dist += 1
        next_level_node = [n for n in next_level_node if n not in visited]
        if next_level_node:
            stack = [list(next_level_node)] + stack
    return cost


costs = {}
costs["AA"] = get_costs("AA")
valves_interest = set([k for k, v in valves.items() if v[0]])
for v in valves_interest:
    costs_from_v = get_costs(v)
    costs[v] = {other_v: c for other_v, c in costs_from_v.items() if other_v in valves_interest}

memory = {}
def max_flow(
    time_remaining: int,
    rate: int,
    released: int,
    pos: str,
    moving: int,
    available_valves: set,
    first_run: bool = False,
) -> int:

    if time_remaining < 0:
        return released

    if moving == 0:
        available_valves = available_valves - set([pos])
        rate += valves[pos][0]

    if first_run:
        estimate_released = released + time_remaining * rate
        state_max = memory.get(tuple(available_valves), 0)
        memory[tuple(available_valves)] = max(estimate_released, state_max)

    released += rate
    time_remaining -= 1

    if not available_valves:
        released += time_remaining * rate
        return released

    # when calculating distance to the next valve don't add 1 (for opening) because time already decreased
    if moving > 0:
        return max_flow(time_remaining, rate, released, pos, moving - 1, available_valves, first_run)

    else:
        # default value for the case no valve is reachable
        flows = [released + time_remaining * rate]
        for me_next in available_valves:
            distance = costs[pos][me_next]
            if distance <= time_remaining:
                flow = max_flow(time_remaining, rate, released, me_next, distance, available_valves, first_run)
                flows.append(flow)
        return max(flows)

# for each set of available valves save the maximum release
# for each of those run a second time for the elefant
result = 0
max_flow(26, 0, 0, "AA", 0, valves_interest, True)
for available, released in memory.items():
    result = max(result, max_flow(26, 0, released, "AA", 0, set(available)))

print("result: ", result)

