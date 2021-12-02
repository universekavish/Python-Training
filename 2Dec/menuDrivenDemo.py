
def add(a, b) : return a + b
def sub(a, b) : return a - b
def mul(a, b) : return a * b
def div(a, b) : return a / b

services = {'1' : add, '2' : sub, '3' : mul, '4' : div}

while True :
	print('\n*****MENU*****\n')
	print('1. Add')
	print('2. Sub')
	print('3. Mul')
	print('4. Div')
	print('5. Exit\n')
	print('\nEnter your choice :', end= '')
	ch = input()
	if ch == '5' :
		print('Bye')
		break
	if int(ch) < 1 or int(ch) > 4 :
		print('Invalid choice...please give me the right choice...')
		continue
		
	a = int(input('Enter first number : '))
	b = int(input('Enter second number : '))
	
	result = services[ch](a, b)
	print('Result : ', result)
	
print('GAME OVER')