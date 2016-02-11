matrix1 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 0, 0]]


def zero_matrix(matrix):
    zero_col = set()
    zero_row = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                zero_col.add(col)
                zero_row.add(row)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in zero_row or col in zero_col:
                matrix[row][col] = 0
    return matrix

print(zero_matrix(matrix1))