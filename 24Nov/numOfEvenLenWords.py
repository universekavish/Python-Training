def numOfEvenLenWords(s) :
    words = s.split()
    count = 0
    for word in words :
        lenOfWord = len(word)

        if lenOfWord % 2 == 0 :
            count = count + 1
        else :
            continue
    return count

s = input('ENter a string to calculate number of even length words : ')

numOfEvenLenWords = numOfEvenLenWords(s)

print('Total Number of even length words are :', numOfEvenLenWords)