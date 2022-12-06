with open("input.txt") as f:
    data = f.read()

data = data.strip()

for i in range(0, len(data)):
    if len(set(data[i:i+4])) == 4:
        print(i+4)
        break

