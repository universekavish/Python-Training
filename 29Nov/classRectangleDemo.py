class Rectangle :
	def __init__(self, x, y) :
		self.length = x
		self.breadth = y
		
	def __str__(self) :
		return 'Rectangle({0}, {1})'.format(self.length, self.breadth)
	
	def area(self) :
		return self.length * self.breadth 
		
	def perimeter(self) :
		return 2*(self.length + self.breadth)
		
	def is_square(self) :
		if self.length == self.breadth :
			return True
		else :
			return False
		
	def scale(self, length = 0, breadth = 0) :
		if self.length + length > 0 :
			self.length = self.length + length
		elif self.breadth + breadth > 0 :
			self.breadth = self.breadth + breadth 
		elif self.length + length > 0 and self.breadth + breadth > 0 :
			self.length = self.length + length
			self.breadth = self.breadth + breadth 
			
	def __add__(self, other) :
		temp = Rectangle(self.length + other.length, self.breadth + other.breadth)
		return temp
		
	def __eq__(self, other) :
		return self.length == other.length and self.breadth == other.breadth
		
#Main App Begins here
R1 = Rectangle(2, 3)
print(R1)

a = R1.area()
print('Area of rectangle is : ', a)

p = R1.perimeter()
print('Perimeter is : ', p)

squareOrNot = R1.is_square()
if squareOrNot :
	print('Is a square')
else :
	print('Not a square')

'''
#Scaling Part
result = R1.scale(length = 3)
print(R1)
result1 = R1.scale(breadth = 5)
print(R1)
result2 = R1.scale(length = 3, breadth = 5)
print(R1)
'''

R2 = Rectangle(2, 3)
R3 = R1 + R2
print(R3)

if R1 == R2 :
	print('Same')
else :
	print('Not samee')

L = [10, 20]
print(L)
S = set(L)
print(S)