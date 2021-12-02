add = lambda a, b : a + b
s = add(2, 3)
print('Sum ', s)

L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8 ,9, 10]

m = map(add, L1, L2)

print(m)
print(list(m))

import functools
r = functools.reduce(add, L1)
print(r)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = map(add, L[::2],L[1::2])
print(list(m))

print('---------------------')
L1 = ['Hi', 'hello', 'Ok', 'fine', 'done', 'apple', 'mad', 'dog']
l2 = sorted(L1)
print(L1)
print(L2)

length = lambda x : len(x)
L3 = sorted(L1, key = length)
print(L3)

L1 = [(30, 20), (10, 20), (-5, 100), (10, 25), (11, 22)]
print(L1)
L2 = sorted(L1)
print(L2)

position = lambda x : x[1]
L3 = sorted(L1, key = position)
print(L3)