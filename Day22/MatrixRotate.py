def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = []

    for i in range(m):
        new_row = []
        for j in range(n):
            new_row.append(matrix[j][i])
        transposed.append(new_row)

    for row in transposed:
        row.reverse()

    return transposed

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = rotate(matrix)
print(rotated)