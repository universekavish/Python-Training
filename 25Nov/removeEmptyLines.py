import sys

if len(sys.argv) != 2 : 
	print('INVALID INPUT')
	sys.exit(1)
	
fin = open('input.txt', 'r')
fout = open('input.txt', 'w')
while True :
    line = fin.readline()
    if len(line) == 0 : break
    for i in fin.readlines() :
        if not i.strip() :
            print(i)
        if i :
            continue