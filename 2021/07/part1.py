with open('input.txt') as f:
    inp = f.read()

positions = list(map(int, inp.split(',')))
max_pos = max(positions)

fuel = max_pos * len(positions)
for i in range(max_pos):
    fuel = min(sum(map(abs, map(lambda x: x - i, positions))), fuel)

print(fuel)
