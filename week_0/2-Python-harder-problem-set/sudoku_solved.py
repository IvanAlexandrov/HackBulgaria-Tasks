DIGITS = [x for x in range(1, 10)]


def sudoku_solved(sudoku):
    # TODO: Think for better algorithm
    if len(sudoku) != 9:
        return "It is not valid sudoku matrix"
    sum_rows = [sum(x) for x in sudoku]
    sum_cols = [sum(x) for x in zip(*sudoku)]

    if sum_rows == sum_cols and sum_rows[0] == 45 and sum_cols[0] == 45:
        result = []
        if is_valid_sudoku_slice([row[0:3] for row in sudoku[0:3]]):
            result.append(True)
        if is_valid_sudoku_slice([row[3:6] for row in sudoku[0:3]]):
            result.append(True)
        if is_valid_sudoku_slice([row[6:9] for row in sudoku[0:3]]):
            result.append(True)
        if is_valid_sudoku_slice([row[0:3] for row in sudoku[3:6]]):
            result.append(True)
        if is_valid_sudoku_slice([row[3:6] for row in sudoku[3:6]]):
            result.append(True)
        if is_valid_sudoku_slice([row[6:9] for row in sudoku[3:6]]):
            result.append(True)
        if is_valid_sudoku_slice([row[0:3] for row in sudoku[6:9]]):
            result.append(True)
        if is_valid_sudoku_slice([row[3:6] for row in sudoku[6:9]]):
            result.append(True)
        if is_valid_sudoku_slice([row[6:9] for row in sudoku[6:9]]):
            result.append(True)
        return len(result) == 9
    return False


def is_valid_sudoku_slice(slice_):
    print(slice_)
    new_list = []
    for slice_row in slice_:
        for slice_col in slice_row:
            new_list.append(slice_col)
    new_list = sorted(new_list)
    return new_list == DIGITS


print(sudoku_solved([
    [4, 5, 2, 3, 8, 9, 7, 1, 6],
    [3, 8, 7, 4, 6, 1, 2, 9, 5],
    [6, 1, 9, 2, 5, 7, 3, 4, 8],
    [9, 3, 5, 1, 2, 6, 8, 7, 4],
    [7, 6, 4, 9, 3, 8, 5, 2, 1],
    [1, 2, 8, 5, 7, 4, 6, 3, 9],
    [5, 7, 1, 8, 9, 2, 4, 6, 3],
    [8, 9, 6, 7, 4, 3, 1, 5, 2],
    [2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
print(sudoku_solved([
    [12, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]))
