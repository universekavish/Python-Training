L = [10, 20, [30, 40], 50]

#Shallow Copy
L1 = L
print(L, L1)
L[0] = 100
print(L, L1)

#Not Shallow not Deep
L2 = L[:]
print(L, L2)
L[0] = 200
print(L, L2)
L[2][0] = 300
print(L, L2)

# Deepcopy
import copy
L3 = copy.deepcopy(L)
print(L, L3)
L[2][0] = 400
print(L, L3)
