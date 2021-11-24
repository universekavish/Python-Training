s = input('Enter a string: ')

words = s.split()
count = 0
for word in words :
    lenOfWord = len(word)

    if lenOfWord % 2 == 0 :
        count = count + 1
    else :
        continue

print('Number of even length words : ', count)