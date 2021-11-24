s = input('Enter IP address to know its class: ')

words = s.split('.')

if int(words[0]) >= 1 and int(words[0]) <= 127 :
    print(s, 'belongs to class A')
elif int(words[0]) >= 128 and int(words[0]) <= 191 :
    print(s, 'belongs to class B')
elif int(words[0]) >= 192 and int(words[0]) <= 223 :
    print(s, 'belongs to class C')
