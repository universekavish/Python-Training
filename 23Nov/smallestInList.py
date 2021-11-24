x = int(input("Enter number of elements: "))

l = []

i = 0
while i < x :
	number = int(input('Enter elements: '))
	l.append(number)
	i = i + 1
print(l)

i = 1
smallest = l[0]
while i < x :
	if l[i] < smallest :
		smallest = l[i]
	i = i + 1
print(smallest)

#Using for loop
smallest = l[0]
for x in l[1:]:
	if x < smallest :
		smallest = x

print(smallest)