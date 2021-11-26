import sys

if len(sys.argv) != 3 : 
    print("ENter valid input ")
    sys.exit(1)

fin = open('matrix1.txt', 'r')
fin2 = open('matrix2.txt', 'r')
matrix1 = []
for line in fin.readlines() :
    a = []
    for num in line.split() :
        a.append(int(num))
    matrix1.append(a)
print(matrix1)

matrix2 = []
for line2 in fin2.readlines() :
    a = []
    for num in line.split() :
        a.append(int(num))
    matrix2.append(a)
print(matrix2)

resultMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

if len(matrix1) == len(matrix2) :
    for i in range(len(matrix1)) :
        for j in range(len(matrix2)) :
            resultMatrix[i][j] = matrix1[i][j] + matrix2[i][j]

print('Sum of ', matrix1, ' and ', matrix2, ' is: ', resultMatrix)