import re

s = 'hello what are you doing 345 hello how are you 4309'
pat = input('Enter some pattern to replace : ')

s1 = re.sub(pat, 'ABC', s)
print(s1)