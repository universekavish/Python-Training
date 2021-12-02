import sys

#def Analyzer() :
#fin = open('shallowCopyDeepCopy')

if len(sys.argv) == 1 : print('Invalid input ')

word = ''
d = {}
def updateD(word) :
	if word not in d : 
		d[word] = 0
	else :
		d[word] = d[word] + 1
		
i = 1
for i in sys.argv : 
	fin = open(i, 'r')
	for line in fin.readlines() :
		words = line.split(' ')
		for word in words : 
			if word == 'import' :
				updateD(word)
			elif word == 'def' :
				updateD(word)
			elif word == 'for' :
				updateD(word)
			elif word == 'while' :
				updateD(word)
			elif word == 'if' :
				updateD(word)
			else :
				break
print(d)