import os

data = os.popen('dir')
records = list(data)

#for windows
count = 0
for record in records[5 : -3] :
    fields = record.split()
    #print(fields)
    if fields[2] == '<DIR>' : count = count + 1
print('Number of subdirs : ', count)