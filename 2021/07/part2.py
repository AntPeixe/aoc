with open('input.txt') as f:
    inp = f.read()

positions = list(map(int, inp.split(',')))
max_pos = max(positions)

def increase_cost(n):
    return (n * n + n) / 2

fuel = increase_cost(max_pos) * len(positions)
for i in range(max_pos):
    fuel = min(sum(map(increase_cost, map(abs, map(lambda x: x - i, positions)))), fuel)

print(fuel)
