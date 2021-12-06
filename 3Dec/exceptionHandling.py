print('hello how are you')
L = [10, 20, 30]

try : 
	import ramesh
	x = int(input('Enter one number : '))
	y = int(input('Enter one another number : '))
	
	z = x / y
	print(z)
	print([10])
	
except ValueError :
	print('I got ValueError')
except IndexError :
	print('I got IndexError')
except ZeroDivisionError :
	print('I got ZeroDivisionError')
except Exception as e :
	print('I got someOther error : ', e)
else :
	print('No exceptions ')
finally :
	print('I work always')
	
print('Rest of the app executes')