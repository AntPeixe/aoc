with open("input.txt") as f:
    data = f.read()

lower_a = ord('a')
upper_a = ord('A')

data_in_lines = list(filter(bool, data.split('\n')))
prio = 0
for idx in range(0, len(data_in_lines), 3):
    lines = data_in_lines[idx:idx+3]

    common = list(set(lines[0]).intersection(set(lines[1])).intersection(set(lines[2])))[0]
    if common.lower() == common:
        prio += ord(common) - lower_a + 1
    else:
        prio += ord(common) - upper_a + 27

print(prio)

