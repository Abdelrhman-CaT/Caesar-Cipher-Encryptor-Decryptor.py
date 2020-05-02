def encode(e) :
	alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
	ALPHA=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	if e in alpha :
		print(alpha[alpha.index(e)+3], end='')
	elif e in ALPHA :
		print(ALPHA[ALPHA.index(e)+3], end='')	
	else:
		print(e , end='')

def decode(d) :
	alpha='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
	ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZAPCDEFGHIJKLMNOPQRSTUVWXYZ'
	if d in alpha :
		print(alpha[alpha.find(d,2)-3], end='')
	elif d in ALPHA :
		print(ALPHA[ALPHA.find(d,2)-3], end='')	
	else:
		print(d , end='')

print("""  _____                            _____ _       _               
/  __ \                          /  __ (_)     | |              
| /  \/ ___  __ _ ___  ___ _ __  | /  \/_ _ __ | |__   ___ _ __ 
| |    / _ \/ _` / __|/ _ \ '__| | |   | | '_ \| '_ \ / _ \ '__|
| \__/\  __/ (_| \__ \  __/ |    | \__/\ | |_) | | | |  __/ |   
 \____/\___|\__,_|___/\___|_|     \____/_| .__/|_| |_|\___|_|   
                                         | |                    
                                         |_|            # Powered by: Mr. CaT\n """)

i=1
while i==1 :
	print('1:Encrypt\n2:Decrypt\n')
	decision=input('What do you need? --> ')
	if decision == '1' :
		word=input('Enter the message to Encrypt --> ')
		for e in word :
			encode(f"{e}")
		print('\n')	
	elif decision == '2' :
		word=input('Enter a message to Decrypt --> ')
		for d in word :
			decode(f"{d}")
		print('\n')		
	else:
		print("Unrecognized Method")
	print('-----------------------------------------------------------------')	