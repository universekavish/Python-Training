def freqOfWords(s) :
    words = s.split()

    d = {}

    for word in words :
	    if word not in d :
		    d[word] = 1
	    else :
		    d[word] = d[word] + 1

    print('Words and their frequencies are')
    for i in d :
	    return i, d[i]

s = input('Enter string to get frequency of its words : ')

word, freqOfWords = freqOfWords(s)
print(word, freqOfWords)