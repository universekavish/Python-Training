class A :
	def f(self) :
		print('classA : def f()')
		
class B :
	def f(self) :
		print('classB : def f()')
		
class C(A, B) :
	def g(self) :
		print('classC : def g()')
		
cobj = C()
cobj.g()
cobj.f()