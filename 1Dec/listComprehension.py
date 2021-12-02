L = [10, 11, 12, 13, 14, 15, 16, 17, 18]
print(L)

L1 = [x for x in L if x % 2 == 0]
print(L1)

ip = '10.20.30.40'
octets = ip.split('.')
print(octets)

octets = [int(octet) for octet in octets]
print(octets)

def isPrime(n) :
	if n < 2 : return False
	i = 2
	while i < n :
		if n % i == 0 : return False
		i = i + 1
	return True
	
import random
primesPositions = [p for p in range(100) if isPrime(random.randint(1, 1000))]
print(primesPositions)

class Matrix :
	def __init__(self, r, c, data) :
		self.rows = r
		self.cols = c
		self.data = data
		
	def __str__(self) :
		#return 'Matrix({0}, {1}, {2})'.format(self.rows, self.cols, self.data)	
		return '\n'.join([' '.join([str(x) for x in row]) for row in self.data])
		
	def get_order(self) :
		return self.rows, self.cols
		
#list of 10 matrices
matrices = [Matrix(5, 5, [[random.randint(1, 100) for i in range(5)] for j in range(5)]) for k in range(10)]

#print(matrices)

for matrix in matrices :
	print(matrix)
	print(matrix.get_order())