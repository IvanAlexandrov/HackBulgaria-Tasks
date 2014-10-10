def sum_matrix(m):
    matrix_sum = 0
    for elements in m:
        for element in elements:
            matrix_sum += element

    return matrix_sum


def main():
    print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

if __name__ == "__main__":
    main()