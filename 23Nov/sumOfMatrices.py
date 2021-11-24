matrix1 = [[1, 2, 3], [4, 6, 3], [2, 5, 5]]

matrix2 = [[1, 4, 2], [6, 2, 2], [6, 2, 7]]

resultMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

if len(matrix1) == len(matrix2) :
    for i in range(len(matrix1)) :
        for j in range(len(matrix2)) :
            resultMatrix[i][j] = matrix1[i][j] + matrix2[i][j]

print('Sum of ', matrix1, ' and ', matrix2, ' is: ', resultMatrix)