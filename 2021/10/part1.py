with open("input.txt") as f:
    data = f.readlines()

data = list(map(str.strip, data))
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
close = {")": "(", "]": "[", "}": "{", ">": "<"}

errors = 0
for line in data:
    rolling = []
    for c in line:
        if c not in close:
            rolling.append(c)
        else:
            if close[c] != rolling[-1]:  # error
                errors += scores[c]
                break
            rolling.pop()
print(errors)
