import numpy as np

# input_file = "day3_test.txt"
input_file = "day3.txt"

with open(input_file) as f:
    data = [list(map(int, list(l.strip()))) for l in f.readlines()]

matrix = np.array(data)

ox = ""
consider = matrix
for col in range(matrix.shape[1]):
    totals = consider.shape[0]
    if len(consider) == 1:
        k = str(consider[0,col])
    else:
        common = sum(consider[:,col])
        k = "1" if common >= totals - common else "0"
    ox += k
    consider = consider[consider[:,col]==int(k)]

co2 = ""
consider = matrix
for col in range(matrix.shape[1]):
    totals = consider.shape[0]
    if len(consider) == 1:
        k = str(consider[0,col])
    else:
        common = sum(consider[:,col])
        k = "0" if common >= totals - common else "1"
    co2 += k
    consider = consider[consider[:,col]==int(k)]

print(int(ox, 2) * int(co2, 2))

"""
s = matrix.sum(axis=0)

gamma = ""
for i, e in enumerate(s):
    if e > totals[i] - e:
        gamma += "1"
    else:
        gamma += "0"

epsilon = "1" * len(gamma)
epsilon = int(epsilon, 2)
gamma = int(gamma, 2)
epsilon = epsilon ^ gamma

print(gamma * epsilon)
"""
