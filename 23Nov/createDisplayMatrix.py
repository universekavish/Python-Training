rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of columns: '))

matrix = []

for i in range(rows) :
	a = []
	for j in range(cols) :
		a.append(int(input()))
	matrix.append(a)
			
print(matrix)
