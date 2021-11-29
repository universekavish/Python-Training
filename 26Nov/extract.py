import re

s = 'hello what are you doing 345 hello how are you 4309'
pat = input('Enter some pattern to extract : ')

result = re.findall(pat, s)
print(result)