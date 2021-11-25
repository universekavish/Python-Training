#DEFAULT ARGS
print('Default Args : ')
def sample(a, b = 0, c = 1) :
	print(a, b, c)

sample(10)
sample(10, 20)
sample(10, 20, 30)


#VARIABLE NUMBER OF ARGS
print('VARIABLE NUMBER OF ARGS : ')
def add(a, b, *t) :
	s = a + b
	for x in t :
		s = s + x
	return s

print(add(1, 2, 3, 4))

#KEY - WORD ARGS
print('KEY - WORD ARGS : ')
def sample2(j, k, l) :
	print(j, k, l)

sample2(j = 'hi', k = 1.5, l = 30)

# VARIABLE NUMBER OF KEY - WORD ARGS
print('VARIABLE NUMBER OF KEY - WORD ARGS : ')
def sample3(**d) :
	print(d)
	
sample3(m = 'Monday')
sample3(m = 'Monday', b = 'Tuesday')
