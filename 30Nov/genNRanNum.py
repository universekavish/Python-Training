import random
import sys

if len(sys.argv) != 2 :
    print('invalid input !!!')
    sys.exit(1)

n = int(sys.argv[1])

i = 0
l = []

while i < n :
    x = random.randint(1, 1000)
    l.append(x)
    i = i + 1

print(l)