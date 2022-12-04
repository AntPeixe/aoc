with open("input.txt") as f:
    data = f.readlines()

data = list(map(str.strip, data))
scores = {")": 1, "]": 2, "}": 3, ">": 4}
close = {")": "(", "]": "[", "}": "{", ">": "<"}
k, v = zip(*close.items())
open = dict(zip(v, k))

errors = []
for line in data:
    rolling = []
    corrupt = False
    for c in line:
        if c not in close:
            rolling.append(c)
        else:
            if close[c] != rolling[-1]:  # error
                corrupt = True
                break
            rolling.pop()

    if corrupt: continue
    print(rolling)

    err = 0
    for i in rolling[::-1]:
        err = err * 5 + scores[open[i]]
    errors.append(err)

print(sorted(errors)[len(errors)//2])

