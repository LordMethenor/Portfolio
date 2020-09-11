import time
import webbrowser
print("\n")
time.sleep(1)
print("\n*********************************************->")
print("*  Welcome to Lee's                           *")
print("*        _____                                *")
print("*       / ____|                               *")
print("*      | |     __ _  ___  ___  __ _ _ __      *")
print("*      | |    / _` |/ _ \/ __|/ _` | '__|     *")
print("*      | |___| (_| |  __/\__ \ (_| | |        *")
print("*       \_____\__,_|\___||___/\__,_|_|        *")
print("*                             Cipher Program  *")
print("***********************************************\n")
time.sleep(1)
continued = True
while continued == True:
	clear_text = input("Type in your message: ")
	shift = int(input("choose your shift (if you are decrypting, use a negative integer): ")) 
	print("")
	input("Press enter to continue.")
	cipher_text = ""
	for c in clear_text:
		if c.isalpha():
			current = ord(c)
			if current >=97:
				current = ord(c) -97
				current += shift
				current = current %26
				current = chr(current +97)
				cipher_text += current
			else:
				current = ord(c) -65
				current += shift
				current = current %26
				current = chr(current +65)
				cipher_text += current
		else:
			cipher_text +=c
	if shift <=-1:
		print("The decrypted message is:",cipher_text)
	else:
		print("The encrypted message is:",cipher_text)
	time.sleep(1)
	restart = input("Do you want to encrypt/decrypt another message? Type Yes or No. ")
	tryagain = True
	while tryagain == True:
		if restart == "Yes":
			tryagain = False
		elif restart == "No":
			print("Goodbye!")
			exit()
		else:
			restart = input("Please try again with either Yes or No. ")
 
