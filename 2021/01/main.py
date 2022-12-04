# input_file = "day1_test.txt"
input_file = "day1.txt"

with open(input_file) as f:
    data = list(map(int, (map(lambda x: x.strip(), f.readlines()))))


count = 0
for i in range(len(data[1:])):
    if len(data[i+1:i+4]) != 3:
        break

    if sum(data[i+1:i+4]) > sum(data[i:i+3]):
        count += 1

print(data)
print(count)
