import sys

if len(sys.argv) != 3 : 
	print('!!Invalid input!!')
	sys.exit(1)

fin = open('input.txt', 'r')
fin2 = open('input2.txt', 'r')

count = 1
while True :
    line = fin.readline()
    line2 = fin2.readline()

    if line != line2 :
        print('Different at ', count, ' line.')
    else :
        print(count)
    count = count + 1