fin = open('data.txt', 'r')
while True :
	line = fin.readline()
	if len(line) == 0 : break
	print(line)
fin.close()