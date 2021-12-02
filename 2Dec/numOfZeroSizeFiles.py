import os
'''
import re
data = os.popen('ls -l')
count = 0
for lines in data.readlines() :
	#pat = '*\s*'
	
	pat = '\d[0]'
	for line in lines :
		if re.search(pat, line) :
			count = count + 1
		else :
			continue
print(count)
'''


data = os.popen('ls -l')
records = list(data)

count = 0

for record in records[1 : ] :
	fields = record.split()
	size = int(fields[4])
	if size == 0 : count = count + 1
	
print('num of zero size files ', count)