import sys

if len(sys.argv) != 3 : 
	print('!!Invalid input!!')
	sys.exit(1)

def copy() :
    fin = open('data.txt', 'r')
    fout = open('copied.txt', 'w')

    while True :
	    line = fin.readline()
	    if len(line) == 0 : break
	    fout.write(line)
    fin.close()
    fout.close()

copy()