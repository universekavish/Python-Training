import os
import time

data = os.popen('ls -l')
print(data)

for x in data :
	print(x, end='')
	time.sleep(1)