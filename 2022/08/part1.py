with open("input.txt") as f:
    data = f.read()

data = list(filter(bool, data.split()))

data = [[int(tree) for tree in line] for line in data]

visible = len(data) * 2 + len(data[0]) * 2 - 4

already_calc = {}
def get_col(data, i):
    if col := already_calc.get(i):
        return col
    col = [row[i] for row in data]
    already_calc[i] = col
    return col
        
for row_idx in range(1, len(data) - 1):
    tree_row = data[row_idx]
    for col_idx in range(1, len(data[0]) - 1):
        tree_col = get_col(data, col_idx)

        tree = data[row_idx][col_idx]

        row_pre = tree_row[:col_idx]
        row_post = tree_row[col_idx+1:]
        col_pre = tree_col[:row_idx]
        col_post = tree_col[row_idx+1:]

        if any(map(lambda x: tree > max(x), [row_pre, row_post, col_pre, col_post])):
            visible += 1

print(visible)

