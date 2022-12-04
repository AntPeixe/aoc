with open("input.txt") as f:
    data = f.read()

lower_a = ord('a')
upper_a = ord('A')

prio = 0
for line in data.split('\n'):
    if not line: continue
    half = len(line) // 2
    first = line[:half]
    second = line[half:]

    common = list(set(first).intersection(set(second)))[0]
    if common.lower() == common:
        prio += ord(common) - lower_a + 1
    else:
        prio += ord(common) - upper_a + 27

print(prio)
