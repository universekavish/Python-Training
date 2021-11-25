def smallest(a, b, c) :
	if x < y :
		if x < z :
			return x
		else :
			return z
	else :
		return y
		
#MAIN APP BEGINS HERE
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))

smallest = smallest(x, y, z)
print(smallest, 'is the smallest')