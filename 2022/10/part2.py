with open("input.txt") as f:
    data = f.readlines()

data = list(map(lambda x: x.strip(), data))

x_reg = 1
current_cycle = 1
crt = ""

for instruction in data:
    crt_pixel = (len(crt) % 40)
    crt += "#" if crt_pixel in range(x_reg - 1, x_reg + 2) else " "

    amount = 0
    if instruction == "noop":
        cycle_increase = 1
    else:
        amount = int(instruction.split()[1])
        cycle_increase = 2

        # do again for the cycle that skips
        crt_pixel = (len(crt) % 40)
        crt += "#" if crt_pixel in range(x_reg - 1, x_reg + 2) else " "

    current_cycle += cycle_increase
    x_reg += amount

for _ in range(6):
    row = crt[:40]
    crt = crt[40:]
    print(''.join(row))

