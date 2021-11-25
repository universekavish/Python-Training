import sys

if len(sys.argv) != 2 : 
	print('Enter valid input')
	sys.exit(1)
	
fin = open('input.txt', 'r')
count = 0
while True :
	line = fin.readline()
	if len(line) == 0 : break
	words = line.split()
	
	for word in words :
		count = count + 1
fin.close()
print(count)