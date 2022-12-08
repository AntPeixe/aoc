with open("input.txt") as f:
    data = f.read()

data = list(filter(bool, data.split()))

data = [[int(tree) for tree in line] for line in data]

already_calc = {}
def get_col(data, i):
    if col := already_calc.get(i):
        return col
    col = [row[i] for row in data]
    already_calc[i] = col
    return col
        
scenic_score = 0
for row_idx in range(1, len(data) - 1):
    tree_row = data[row_idx]
    for col_idx in range(1, len(data[0]) - 1):
        tree_col = get_col(data, col_idx)

        tree = data[row_idx][col_idx]

        row_pre = tree_row[:col_idx][::-1]
        row_post = tree_row[col_idx+1:]
        col_pre = tree_col[:row_idx][::-1]
        col_post = tree_col[row_idx+1:]

        tree_score = 1
        for direction in [row_pre, row_post, col_pre, col_post]:
            dir_score = 0
            for t in direction:
                dir_score += 1
                if t >= tree:
                    break
            tree_score *= dir_score

        scenic_score = max(scenic_score, tree_score)

print(scenic_score)

