import random
lenL = 0
elements = []
i = 0
while i < 10:
	element = random.randint(1, 100)
	while True : 
		element2 = random.randint(1, 100)
		if element2 == element :
			elements.append(element2)
			print('appended')
			lenL = lenL + 1
		else :
			elements.clear()
			print('cleared')
			lenL = 0
			break
	break
print(elements)