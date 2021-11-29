import re

s = 'hello what are you doing 345 hello how are you'
pat = input('Enter some pattern to search : ')

if re.search(pat, s) :
	print('Found!!')
else : 
	print('Not found')