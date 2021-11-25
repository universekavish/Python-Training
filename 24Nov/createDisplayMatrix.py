def createMatrix() :
	print('***TO CREATE MATRIX***')
	rows = int(input('Enter number of rows: '))
	cols = int(input('Enter number of columns: '))
	
	matrix = []
	
	for i in range(rows) :
		a = []
		for j in range(cols) :
			a.append(int(input()))
		matrix.append(a)
	return matrix
		
matrix1 = createMatrix()
print('matrix1: ', matrix1)
matrix2 = createMatrix()
print('matrix2: ', matrix2)