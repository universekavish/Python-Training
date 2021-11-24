s = input("Enter string with duplicate words: ")

words = s.split()

d = {}
l = []

for word in words :
	if word not in d :
		d[word] = 1
		l.append(word)
		
# l = d.keys()

result = ' '.join(l)
print('result: ', result)