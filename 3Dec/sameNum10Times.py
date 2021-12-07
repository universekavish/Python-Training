#import sys
import random
l = []

'''
while True : 
	
	if len(l) == 10 : break
	element1 = random.randint(1, 5)
	while True : 
		if len(l) == 10 : break
		element2 = random.randint(1, 5)
	
		if element2 == element1 :
			l.append(element2)
			print('appended ', element2)
			print(l)
		else :
			l.clear()
print(l)
'''

while True : 
	
	if len(l) == 10 : break
	element1 = random.randint(1, 2)
	while True : 
		if len(l) == 10 : break
		element2 = random.randint(1, 2)
	
		if element2 == element1 :
			l.append(element2)
			print('appended ', element2)
			print(l)
		else :
			l.clear()
			element1 = element2
print(l)