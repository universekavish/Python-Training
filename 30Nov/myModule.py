'''
This module contains the following services :
1) data : version, L
2) functions : sayHi, sayHello
3) classes : Rectangle, Person, Employee
'''

version = 1
L = [10, 20, 30]

def sayHi() :
	'''
	sayHi method ---> Hi...
	'''
	print('Hi...')
	
def sayHello() :
	'''
	sayHello method ---> Hello...
	'''
	print('Hello...')
	
class Rectangle :
	'''
	Documentation for Rectangle class :
	1) functions : area, perimeter, is_square, scale
	'''
	def __init__(self, x, y) :
		self.length = x
		self.breadth = y
		
	def __str__(self) :
		return 'Rectangle({0}, {1})'.format(self.length, self.breadth)
	
	def area(self) :
		'''
		area method returns area of Rectangle
		'''
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
		
class Person :
	def __init__(self, fname, lname, email) :
		self.fname = fname
		self.lname = lname
		self.email = email
		
	def __str__(self) :
		return 'Person({0}, {1}, {2})'.format(self.fname, self.lname, self.email)
		
	def fullname(self) :
		return self.fname + ' ' + self.lname
		
	def get_email(self) :
		return self.email

class Employee(Person) :
	def __init__(self, fname, lname, email, eid, salary) :
		Person.__init__(self, fname, lname, email)
		self.eid = eid
		self.salary = salary
		
	def __str__(self) :
		return 'Employee({0}, {1}, {2}, {3}, {4})'.format(self.fname, self.lname, self.email, self.eid, self.salary)
		
	def getsalary(self) : return self.salary