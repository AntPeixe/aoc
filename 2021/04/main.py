import numpy as np

# input_file = "day4_test.txt"
input_file = "day4.txt"

with open(input_file) as f:
    data = f.readlines()

numbers = list(map(int, data[0].strip().split(",")))

boards = []
board = []
for l in data[2:]:  # start on 2 because 1 is the empty line between numbers and first board
    l = l.strip()
    if l:
        board.append(list(map(int, l.split())))
    else:
        boards.append(board)
        board = []
boards.append(board)  # there is no empty line at end, append last board
boards = np.array(boards)

marks = np.zeros(boards.shape, dtype=np.bool)

for number in numbers:
    marks = marks | (boards == number)
    cols_sums = marks.sum(axis=1)
    rows_sums = marks.sum(axis=2)

    # check_rows
    # completed_rows = (rows_sums == 5).sum(axis=1).astype(np.bool)
    # table_with_complete_row = completed_rows.tolist().index(True) if any(completed_rows) else -1
    # completed_cols = (cols_sums == 5).sum(axis=1).astype(np.bool)
    # table_with_complete_col = completed_cols.tolist().index(True) if any(completed_cols) else -1
    completed_rows = (rows_sums == 5).sum(axis=1).astype(np.bool)
    completed_cols = (cols_sums == 5).sum(axis=1).astype(np.bool)
    tables_with_completed_rows = [i for i in range(len(completed_rows)) if completed_rows[i]]
    tables_with_completed_cols = [i for i in range(len(completed_cols)) if completed_cols[i]]
    completed_tables = list(set(tables_with_completed_rows + tables_with_completed_cols))

    for index in sorted(completed_tables, reverse=True):
        board = boards[index,:,:]
        mark = marks[index,:,:]
        last_n = number
        boards = np.delete(boards, index, axis=0)
        marks = np.delete(marks, index, axis=0)

    """
    index = max(table_with_complete_row, table_with_complete_col)
    if index != -1:
        if boards.shape[0] == 1:
            board = boards[0,:,:]
            mark = marks[0,:,:]
        else:
            board = boards[index,:,:]
            mark = marks[index,:,:]
            boards = np.delete(boards, index, axis=0)
            marks = np.delete(marks, index, axis=0)
    """

print(board, mark, last_n)
unmarked = (~ mark).astype(np.int)
unmarked_sum = (unmarked * board).sum()
print(unmarked)
print(unmarked_sum * last_n)

