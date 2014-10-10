def magic_square(matrix):
    matrix_lenght = len(matrix)
    rows_sum = [sum(x) for x in matrix]
    cols_sum = [sum(x) for x in zip(*matrix)]
    diagonal_l_sum = sum(matrix[i][i] for i in range(0, matrix_lenght))
    diagonal_r_sum = sum(matrix[matrix_lenght-1- i][i] for i in range(matrix_lenght-1, -1, -1))
    # print(rows_sum, cols_sum, diagonal_l_sum, diagonal_r_sum)
    if rows_sum != cols_sum or diagonal_l_sum != diagonal_r_sum:
        return False
    else:
        return True

print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print(magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5],[9, 6, 15, 4]]))
print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
