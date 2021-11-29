
import sys
import re

if len(sys.argv) != 2 :
	print('invalid input')
	sys.exit(1)
	
def extract(pat, s) :
	return re.findall(pat, s)

s = 'hello What are you doing 345 87 98 89999 Hello how ArE you 43.09'
pat = sys.argv[1]

#pat = ['[A-Z]\w+', '[A-Z]\w+[a-z]', '\w*[aeiouAEIOU]+\w+', '\d+.\d+', '\d{2,4}[13579]']

result = extract(pat, s)
print(result)