x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))

if x < y :
	if x < z :
		print(x, 'is the smallest')
	else :
		print(z, 'is the smallest')
else :
	print(y, 'is the smallest')