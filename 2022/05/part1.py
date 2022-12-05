with open("input.txt") as f:
    data = f.read()

crates_input, moves = list(map(lambda x: x.split('\n'), data.split('\n\n')))

stacks = [[] for _ in range(len(crates_input[-1].split()))]

for line in crates_input[:-1][::-1]:
    # go over crates in reverse
    for idx, s in enumerate(stacks):
        if (crate := line[idx * 4 + 1]) != ' ':
            s.append(crate)
            
for move in moves:
    if not move: continue
    move = move.split()
    quant, start, end = int(move[1]), int(move[3]), int(move[5])

    for _ in range(quant):
        crate = stacks[start - 1].pop()
        stacks[end - 1].append(crate)


print(''.join([s.pop() for s in stacks]))

