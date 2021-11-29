import sys

if len(sys.argv) != 3 : 
	print('!!Invalid input!!')
	sys.exit(1)

fin = open('input.txt', 'r')
fin2 = open('input2.txt', 'r')

differentLine = []
count = 1
while True :
    line = fin.readline()
    line2 = fin2.readline()

    for line in fin.readlines() :
        for line2 in fin2.readlines() :
            if line == line2 :
                print('Same at : ', count)
            else :
                differentLine.append(count)
        count = count + 1
    print('different at ', differentLine)
    # i = 0; j = 0
    # while i < len(line) and j < len(line2) :
    #     if line[i] != line2[j] :
    #         i = i + 1
    #         j = j + 1
    #         print('Im good')
    #         differentLine.append(count)
    #     else : 
    #         i = i + 1
    #         j = j + 1
    #     count = count + 1
print('Different at lines : ', differentLine)