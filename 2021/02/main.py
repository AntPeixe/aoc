# input_file = "day2_test.txt"
input_file = "day2.txt"

with open(input_file) as f:
    data = [l.strip() for l in f.readlines()]

h, d, aim = 0, 0, 0
for l in data:
    k, a = l.split()
    a = int(a)
    if k == "forward":
        h += a
        d += aim * a
    elif k == "up":
        aim -= a
    elif k == "down":
        aim += a

print(h*d)
