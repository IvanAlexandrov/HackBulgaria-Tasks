from sum_matrix import sum_matrix


def matrix_bombing_plan(matrix):
    result = {}
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            # print(new_matrix)
            new_matrix = [x[:] for x in matrix]
            key = (i, j)
            subtraction = matrix[i][j]
            # upper center element
            update_matrix(new_matrix, i - 1, j, subtraction)
            # upper left element
            update_matrix(new_matrix, i - 1, j - 1, subtraction)
            # upper right elemet
            update_matrix(new_matrix, i - 1, j + 1, subtraction)
            # left element
            update_matrix(new_matrix, i, j + 1, subtraction)
            # right element
            update_matrix(new_matrix, i, j - 1, subtraction)
            # bottom center element
            update_matrix(new_matrix, i + 1, j, subtraction)
            # bottom left element
            update_matrix(new_matrix, i + 1, j + 1, subtraction)
            # bottom right element
            update_matrix(new_matrix, i + 1, j - 1, subtraction)
            result[key] = sum_matrix(new_matrix)
    return  sorted(result.items()) #result


def update_matrix(matrix, x, y, subtraction):  # void method
    # if positions are not in ranges return None
    if x < 0 or \
       y < 0 or \
       x >= len(matrix[0]) or \
       y >= len(matrix):
            return
    if matrix[x][y] - subtraction < 0:
        matrix[x][y] = 0
    else:
        matrix[x][y] -= subtraction

print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(matrix_bombing_plan([[10, 10, 10], [10, 9, 10], [10, 10, 10]]))
