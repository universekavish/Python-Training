import sys

if len(sys.argv) != 3 :
	print('INVALID input, Enter valid input')
	sys.exit(1)

x = int(sys.argv[1])
y = int(sys.argv[2])

z = x + y
print('Sum of ', x, ' and ', y, ' is : ', z)