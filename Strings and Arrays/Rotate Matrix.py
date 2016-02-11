matrix1 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

def rotate_matrix(matrix):
    n = len(matrix)

    for layer in range(int(n / 2)):
        first = layer
        last = n - 1 - layer

        for idx in range(first, last):
            offset = idx - first
            top = matrix[first][idx]

            #left to top
            matrix[first][idx] = matrix[last - offset][first]

            #bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]

            #right to bottom
            matrix[last][last - offset] = matrix[first + offset][last]

            #top to right
            matrix[first + offset][last] = top
    return matrix
print(rotate_matrix(matrix1))