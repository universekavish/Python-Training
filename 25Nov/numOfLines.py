import sys

if len(sys.argv) != 2 : 
	print('Invalid input: ')
	sys.exit(1)

fin = open('input.txt', 'r')

count = 0
while True :
	line = fin.readline()
	if len(line) == 0 : break
	count = count + 1
fin.close()
print(count)