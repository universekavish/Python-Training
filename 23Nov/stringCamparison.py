string1 = input('Enter first string: ')
string2 = input('Enter second string: ')

print(len(string1))
print(len(string2))

l = []

if string1 == string2 :
	print('Same string')
else :
	i = 0; j = 0
	while i < len(string1) and j < len(string2):
		if string1[i] != string2[j] :
			l.append(i)
			i = i + 1
			j = j + 1
		else :
			i = i + 1
			j = j + 1
	print('Different at indexes: ', l)