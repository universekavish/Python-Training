import sys 

if(len(sys.argv)) != 2 :
	print('Enter valid input')
	sys.exit(1)
	
fin = open('input.txt', 'r')
d = {}
while True :
	
	line = fin.readline() 
	if len(line) == 0 : break
	words = line.split()
	i = 0
	for word in words :
		for i in word :
			if i not in d :
				d[i] = 1
			else :
				d[i] = d[i] + 1
fin.close()
print(d)

length = len(d)

valueList = d.values()
print(valueList)
Lv = list(valueList)

j = 1
smallest = int(Lv[0])
while j < length :
	if Lv[j] < smallest :
		smallest = Lv[j]
	j = j + 1

def get_key(val):
    for key, value in d.items():
         if val == value:
             return key
    return "key doesn't exist"

print(get_key(smallest), ' is with minimum occurence ', smallest)

k = 1
biggest = int(Lv[0])
while k < length :
	if Lv[k] > biggest :
		biggest = Lv[k]
	k = k + 1
print(get_key(biggest), ' is with maximum occurence ', biggest)