from itertools import zip_longest

with open("input.txt") as f:
    data = f.readlines()

data = [line.strip() for line in data]
data = list(filter(bool, data))

def compare_two(left, right):
    # -1 left smaller / 0 equal / 1 right smaller
    
    if left is None: return -1
    if right is None: return 1

    if isinstance(left, int) and isinstance(right, int):
        if left == right: return 0
        return -1 if left < right else 1

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for element_left, element_right in zip_longest(left, right):
        cmp = compare_two(element_left, element_right)
        if cmp != 0: return cmp

    # they were the same till the end
    return 0

ordered_packets = [[[2]], [[6]]]
while data:
    new_packet = eval(data.pop(0))

    for idx, packet in enumerate(ordered_packets):
        cmp = compare_two(new_packet, packet)
        if cmp == -1:
            ordered_packets.insert(idx, new_packet)
            break
    else:
        ordered_packets.append(new_packet)

a, b = [idx + 1 for idx, packet in enumerate(ordered_packets) if packet == [[2]] or packet == [[6]]]
print(a*b)

