import re 

s = 'hello 34 hello hi 566 meet 600'
pat = input('Enter pattern ')
result = re.findall(pat, s)
sum = 0

for i in result :
	sum = sum + int(i)
	
print(sum)