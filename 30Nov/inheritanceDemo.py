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
	
#Main app begins here
p = Person('Kavish', 'Boyal', 'kavish@boyal.com')
print(p)

fn = p.fullname()
print('p fullname ', fn)

emp = Employee('Kavish', 'Boyal', 'kavish@boyal.com', 12345, 10000)
print(emp)

fn  = emp.fullname()
print('emp fullname ', fn)

sal = emp.getsalary()
print('emp salary is ', sal)