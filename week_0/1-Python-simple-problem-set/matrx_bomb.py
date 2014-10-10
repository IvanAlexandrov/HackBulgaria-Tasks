from sum_matrix import sum_matrix
def matrix_bombing_plan(m):
    new_matrix = m
    result = {}
    row = 0
    for elements in m:
        for element in elements:
            dropping_place = element
            break
        col = 0
        for old_element in elements:
            if dropping_place == old_element:
                new_matrix[row][col] = old_element
            else:
                new_element = old_element - dropping_place
                if new_element < 0:
                    new_element = 0
                new_matrix[row][col] = new_element
            key = (row, col)
            result[key] = sum_matrix(new_matrix)
            col += 1
            # print(new_matrix)
        row += 1
    return result

print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
