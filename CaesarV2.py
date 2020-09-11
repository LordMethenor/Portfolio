import time
import random
class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'
def menuopts(shiftmode, shiftkey):
	time.sleep(1)
	print("Please select one of the following:")
	time.sleep(.5)
	print("")
	print("	1-Encrypt a message")
	print("")
	time.sleep(.5)
	print("	2-Decrypt a message")
	print("")
	time.sleep(.5)
	print("	3-Change your shift mode")
	print("")
	time.sleep(.5)
	print("	4-Exit the program ")
	print("")
	print("")
	time.sleep(.5)
	task1 = input("Selection: ")
	confirm1 = input("Press enter to confirm your selection or enter an alternative selection.")
	if confirm1 == "":
		reloop = True
	else:
		task1 = confirm1
		reloop = True
	time.sleep(.5)
	while reloop == True:
		if task1 == "1":
			encrypt(shiftmode, shiftkey)
			reloop = False
		elif task1 == "2":
			if shiftmode == 3 and shiftkey == "":
				task1 = input("You can't use automatic decryption without a saved key. Either encrypt a message to generate a new key (1) or change your shift mode (3).")
				reloop = True
			else:
				decrypt(shiftmode, shiftkey)
				reloop = False
		elif task1 == "3":
			shifter(shiftkey)
			reloop = False
		elif task1 == "4":
			exit()
		else:
			task1 = input("Please try again with either 1, 2, 3, or 4. ")
def shifter(shiftkey):
	print("")
	time.sleep(1)
	print("Choose your shift mode:")
	print("")
	time.sleep(.5)
	print("1-Manual Shift [Default]: Manually select a shift value to encrypt and decrypt your message.")
	print("")
	time.sleep(.5)
	print("2-Manual Key: Input a 12 character key (unicode only) to encrypt and decrypt your message.")
	print("")
	time.sleep(.5)
	print("3-Automatic: Randomly generate a key that will encrypt and decrypt your message.")
	print("")
	time.sleep(.5)
	print("4-Brute Force: Encrypts and decrypts messages using all 26 possible shifts. Choose this if you don't have or want to use a key or shift value.")
	print("")
	print("")
	time.sleep(.5)
	shiftmode = input("Shift Mode: ")
	reloopshift = True
	time.sleep(.25)
	confirm1 = input("Press enter to confirm your selection or enter an alternative selection.")
	if confirm1 == "":
		reloopshift = True
	else:
		task1 = confirm1
	time.sleep(.5)
	while reloopshift == True:
		if shiftmode == "1":
			shiftmode = 1
			reloopshift = False
			menuopts(shiftmode, shiftkey)
		elif shiftmode == "2":
			shiftmode = 2
			reloopshift = False
			menuopts(shiftmode, shiftkey)
		elif shiftmode == "3":
			shiftmode = 3
			reloopshift = False
			menuopts(shiftmode, shiftkey)
		elif shiftmode == "4":
			shiftmode = 4
			reloopshift = False
			menuopts(shiftmode, shiftkey)
		else:
			shiftmode = input("Please try again with either 1, 2, or 3. ")
def encrypt(shiftmode, shiftkey):
	print("")
	time.sleep(1)
	clear_text = input("Type in your message: ")
	time.sleep(.5)
	legit = False
	while legit == False:
		if(clear_text == "" or clear_text == " "):
			clear_text = input("Please type in a non-blank message: ")
		else:
			legit = True
	print("")
	if shiftmode == 1:
		shift = input("Choose your shift: ")
		shiftstest = True
		while shiftstest == True:
			if shift.isdigit() == True:
				shift = int(shift)
				shiftstest = False
			else:
				shift = input("Please try again with an integer shift: ")
		shiftkey = ""
	elif shiftmode == 2:
		tempshift = input("Enter your 12 character key: ")
		relooptempshift = True
		while relooptempshift == True:
			if len(tempshift) == 12:
				relooptempshift = False
			else:
				tempshift = input("Please try again with a 12 alphanumerical character key: ")
		shift = 0
		shiftkey = tempshift
		for c in tempshift:	
			shift = ord(c)+shift
	elif shiftmode == 3:
		time.sleep(.5)
		siftkey = []
		shift = 0
		couinter = 0
		for i in range(0,12):
			siftkey.append(random.randint(33,126))
			shift = siftkey[couinter]+shift
			couinter = couinter+1
		shiftkey = "".join(chr(x) for x in siftkey)
		print("Your key is:",color.BOLD+shiftkey+color.END)
	else:
		shiftkey = ""
		shift = 0
	print("")
	time.sleep(.25)
	input("Press enter to continue.")
	print("")
	cipher_text = ""
	time.sleep(1)
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
	if shiftmode == 1 or shiftmode == 2 or shiftmode == 3:
		print("The encrypted message is:",color.BOLD+cipher_text+color.END)
		print("")
		if shiftmode == 3 or shiftmode == 2:
			menuopts(shiftmode, shiftkey)
		else:
			menuopts(shiftmode, "")
	else:
		print("The encrypted message is:")
		print("")
		shift = 1
		for x in range(0,26):
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
					cipher_text += c
			print("  Key of",shift,": ",color.BOLD+(cipher_text)+color.END)
			shift = shift+1
			print("")
		print("")	
		menuopts(shiftmode, "")
def decrypt(shiftmode, shiftkey):
	print("")
	time.sleep(1)
	clear_text = input("Type in the encrypted message: ")
	time.sleep(.5)
	legit = False
	while legit == False:
		if(clear_text == "" or clear_text == " "):
			clear_text = input("Please type in a non-blank message: ")
		else:
			legit = True
	print("")
	if shiftmode == 1:
		shift = input("Enter the shift used to encrypt the message: ")
		shiftstest = True
		while shiftstest == True:
			if shift.isdigit() == True:
				shift = -int(shift)
				shiftstest = False
			else:
				shift = input("Please try again with an integer shift: ")
		shiftkey = ""
	elif shiftmode == 2:
		tempshift = input("Enter your 12 character key: ")
		relooptempshift = True
		while relooptempshift == True:
			if len(tempshift) == 12:
				relooptempshift = False
			else:
				tempshift = input("Please try again with a 12 alphanumerical character key: ")
		supertempshift = 0
		shiftkey = tempshift
		for c in tempshift:	
			supertempshift = ord(c)+supertempshift
		shift = -supertempshift
	elif shiftmode == 3:
		time.sleep(.5)
		tempshift = 0
		for c in shiftkey:	
			tempshift = ord(c)+tempshift
		shift = -tempshift
	else:
		shiftkey = ""
		shift = 0
	print("")
	time.sleep(.25)
	input("Press enter to continue.")
	print("")
	cipher_text = ""
	time.sleep(1)
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
	if shiftmode == 1 or shiftmode == 2 or shiftmode == 3:
		print("The decrypted message is:",color.BOLD+(cipher_text)+color.END)
		print("")
		if shiftmode == 3 or shiftmode == 2:
			menuopts(shiftmode, shiftkey)
		else:
			menuopts(shiftmode, "")
	else:
		print("The decrypted message is:")
		print("")
		shift = 1
		for x in range(0,26):
			cipher_text = ""
			for c in clear_text:
				if c.isalpha():
					current = ord(c)
					if current >=97:
						current = ord(c) -97
						current -= shift
						current = current %26
						current = chr(current +97)
						cipher_text += current
					else:
						current = ord(c) -65
						current -= shift
						current = current %26
						current = chr(current +65)
						cipher_text += current
				else:
					cipher_text += c
			print("  Key of",shift,": ",color.BOLD+(cipher_text)+color.END)
			shift = shift+1
			print("")
		print("")	
		menuopts(shiftmode, "")
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
print("*                          Cipher Program v2  *")
print("***********************************************\n")
menuopts(1, "")