def evenOdd(a) :
	if a % 2 == 0 : return 'Even'
	return 'ODD'
	
#MAIN APP STARTS HERE
a = int(input('Enter number to find if it is even or odd: '))
evenOdd = evenOdd(a)
print(a, ' is ', evenOdd)