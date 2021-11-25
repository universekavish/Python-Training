#Vaild IP Function
def validateIPV4(ip) :
	octets = ip.split('.')
	n = len(octets)
	if(n != 4) : return False
	for octet in octets :
		if not octet.isdigit() : return False
		
		x = int(octet)
		if x < 1 or x > 255 : return False
	return True
	
# Function to know get class
def get_class(ip):
	if not validateIPV4(ip): return 'Invalid'
	octets = ip.split('.')
	x = int(octets[0])
	if x >= 1 and x <= 126 :
		return 'classA'
	elif x >= 128 and x <= 191 :
		return 'classB'
	elif x >= 192 and x <= 223 :
		return 'classC'
	elif x >= 224 and x <= 239 :
		return 'classD'
	elif x >= 240 and x <= 254 :
		return 'classE'
	
# Function to classify IPs
def classfyIPs(*ips) :
	d = {'classA' : [], 'classB' : [], 'classC' : [], 'classD' : [], 'classE' : [], 'Invalid' : []}
	
	for ip in ips :
		classOfIp = get_class(ip)
		d[classOfIp].append(ip)
		
	return d
	
#MAIN APP BEGINS HERE
ip = input('Enter IP address to process : ')

#r = validateIPV4(ip)

#if r : 
#	print(ip, 'is VALID!!')
#else : 
#	print(ip, 'is INVALID!!')
	
#classOfIp = get_class(ip)
#print(classOfIp)

classifiedIPs = classfyIPs('100.12.21.2' , '234.235.23.23', '1.2.3')
print(classifiedIPs)