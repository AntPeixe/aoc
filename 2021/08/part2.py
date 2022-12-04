with open("input.txt") as f:
    data = f.readlines()
data = [line.strip().split(' | ') for line in data]

segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

total = 0
for line in data:
    signals = line[0].split()

    one = [s for s in signals if len(s) == 2][0]
    seven = [s for s in signals if len(s) == 3][0]
    four = [s for s in signals if len(s) == 4][0]
    eight = [s for s in signals if len(s) == 7][0]
    zero_six_nine = [s for s in signals if len(s) == 6]

    a = set(seven) - set(one)
    e_g = set(eight) - set(four) - a
    c_f = set(one)
    b_d = set(eight) - set(seven) - e_g
    a_b_f_g = set(zero_six_nine[0]) & set(zero_six_nine[1]) & set(zero_six_nine[2])

    g = a_b_f_g - a - c_f - b_d
    b = a_b_f_g - a - c_f - e_g
    f = a_b_f_g - a - b_d - e_g
    c = c_f - f
    d = b_d - b
    e = e_g - g

    mapping = {
        a.pop(): 'a',
        b.pop(): 'b',
        c.pop(): 'c',
        d.pop(): 'd',
        e.pop(): 'e',
        f.pop(): 'f',
        g.pop(): 'g',
    }

    value = ''
    for idx, out_val in enumerate(line[1].split()):
        value += str(segments.index(''.join(sorted([mapping[l] for l in out_val]))))
    total += int(value)

print(total)
