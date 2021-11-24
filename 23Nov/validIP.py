enteredIP = input('Enter IP address to check validity :')

if enteredIP.count('.') == 3 :
    isValid = False
    for i in enteredIP.split('.') :
        if int(i) >= 0 and int(i) <= 255 :    
            isValid = True
        else :
            isValid = False
            break
else :
    isValid = False

if isValid == True :
    print(enteredIP, 'is valid ip address')
else :
    print(enteredIP, 'is NOT a valid Ip address')