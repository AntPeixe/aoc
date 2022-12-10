with open("input.txt") as f:
    data = f.readlines()

data = list(map(lambda x: x.strip(), data))

x_reg = 1
current_cycle = 1
strenght = {}
important_cycles = [20, 60, 100, 140, 180, 220]
for instruction in data:
    if not important_cycles: break
    amount = 0
    if instruction == "noop":
        cycle_increase = 1
    else:
        amount = int(instruction.split()[1])
        cycle_increase = 2

    if current_cycle == important_cycles[0] or current_cycle + 1 == important_cycles[0]:
        strenght[important_cycles[0]] = x_reg
        important_cycles.pop(0)

    current_cycle += cycle_increase
    x_reg += amount

print(sum([c * s for c, s in strenght.items()]))

