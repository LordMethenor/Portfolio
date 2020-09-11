import time
import subprocess
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
#Morse Code Program

#string to convert

#convert process with string replace method
def encrypt():
	time.sleep(.5)
	userText = input("Enter the message you want to convert: ")
	clearText = ""
	reject = False
	for c in userText:
		if c.isalpha() == True:
			if c.isupper() == True:
				c = c.lower()
				reject = True
			else:
				c = c
			clearText += c
		elif c.isspace() == True or c.isdigit() == True or c == "." or c == "/" or c == "'" or c == "," or c == "!" or c == "?":
			clearText += c
		else:
			print("Character",color.BOLD+c+color.END,"rejected.")
			reject = True
	if reject == True:
		time.sleep(.25)
		print("")
		print("Your corected input is: ",color.BOLD+clearText+color.END)
		reject = False
	else:
		reject = False
	temp1 = clearText.replace(" ", "$")
	temp2 = temp1.replace(".", ".-.-.- ")
	temp1 = temp2.replace("/", "-..-. ")
	temp2 = temp1.replace("'", ".---. ")
	temp1 = temp2.replace(",", "--..-- ")
	temp2 = temp1.replace("!", "-.-.-- ")
	temp1 = temp2.replace("?", ".-..-. ")
	temp3 = temp1.replace("a", '.- ')
	temp2 = temp3.replace("b", "-... ")
	temp1 = temp2.replace("c", "-.-. ")
	temp2 = temp1.replace("d", "-.. ")
	temp1 = temp2.replace("e", ". ")
	temp2 = temp1.replace("f", "..-. ")
	temp1 = temp2.replace("g", "--. ")
	temp2 = temp1.replace("h", ".... ")
	temp1 = temp2.replace("i", ".. ")
	temp2 = temp1.replace("j", ".--- ")
	temp1 = temp2.replace("k", "-.- ")
	temp2 = temp1.replace("l", ".-.. ")
	temp1 = temp2.replace("m", "-- ")
	temp2 = temp1.replace("n", "-. ")
	temp1 = temp2.replace("o", "--- ")
	temp2 = temp1.replace("p", ".--. ")
	temp1 = temp2.replace("q", "--.- ")
	temp2 = temp1.replace("r", ".-. ")
	temp1 = temp2.replace("s", "... ")
	temp2 = temp1.replace("t", "- ")
	temp1 = temp2.replace("u", "..- ")
	temp2 = temp1.replace("v", "...- ")
	temp1 = temp2.replace("w", ".-- ")
	temp2 = temp1.replace("x", "-..- ")
	temp1 = temp2.replace("y", "-.-- ")
	temp2 = temp1.replace("z", "--.. ")
	temp1 = temp2.replace("1", ".---- ")
	temp2 = temp1.replace("2", "..--- ")
	temp1 = temp2.replace("3", "...-- ")
	temp2 = temp1.replace("4", "....- ")
	temp1 = temp2.replace("5", "..... ")
	temp2 = temp1.replace("6", "-.... ")
	temp1 = temp2.replace("7", "--... ")
	temp2 = temp1.replace("8", "---.. ")
	temp1 = temp2.replace("9", "----. ")
	temp2 = temp1.replace("0", "----- ")
	temp1 = temp2.replace ("$", "/ ")
	cipherText = temp1
	time.sleep(.5)
	playSound = input("Conversion completed. Do you want to hear audio (Y/n)? ")
	soundConfirm = False
	while soundConfirm == False:
		if playSound == 'Y' or playSound == 'n':
			soundConfirm = True
		else:
			playSound = input("Please enter either Y or n. ")
	print("")
	print("Converted message:", cipherText)
	if playSound == 'Y':
		time.sleep(.5)
		print("")
		print("Now Playing...")
		time.sleep(.25)
		for c in cipherText:
			if c == "-":
				subprocess.call(["afplay", "sounds/dah.wav"])
			elif c == ".":
				subprocess.call(["afplay", "sounds/dit.wav"])
			elif c == "/":
				time.sleep(.2)
			else:
				useless = True
				time.sleep(.25)
	input("Press enter to continue. ")
	print("")
	menuopts()
def decrypt():
	time.sleep(.5)
	cipherText = input("Enter the message you want to decrypt: ")
	textVerified = False
	while textVerified == False:
		cVerified = True
		for c in cipherText:
			if c == '-' or c == '.' or c == ' ' or c== '/':
				c = c
			else:
				cVerified = False
		if cVerified == False:
			cipherText = input("Please try again with morse code compatible characters (- . /) and spaces.")
		else:
			textVerified = True
	if cipherText.endswith(' ') == True:
		cipherText = cipherText	
	else:
		cipherText = cipherText + " "
	temp1 = cipherText.replace(".-.-.- ", "@")
	temp2 = temp1.replace("--..-- ", ",")
	temp1 = temp2.replace("-.-.-- ", "!")
	temp2 = temp1.replace(".-..-. ", "?")
	temp1 = temp2.replace("-..-. ", "$")
	temp2 = temp1.replace(".---. ", "'")
	temp1 = temp2.replace(".---- ", "1")
	temp2 = temp1.replace("..--- ", "2")
	temp1 = temp2.replace("...-- ", "3")
	temp2 = temp1.replace("....- ", "4")
	temp1 = temp2.replace("..... ", "5")
	temp2 = temp1.replace("-.... ", "6")
	temp1 = temp2.replace("--... ", "7")
	temp2 = temp1.replace("---.. ", "8")
	temp1 = temp2.replace("----. ", "9")
	temp2 = temp1.replace("----- ", "0")
	temp1 = temp2.replace("...- ", "v")	
	temp2 = temp1.replace(".... ", "h")
	temp1 = temp2.replace("..-. ", "f")
	temp2 = temp1.replace(".-.. ", "l")	
	temp1 = temp2.replace(".--. ", "p")
	temp2 = temp1.replace(".--- ", "j")	
	temp1 = temp2.replace("--.- ", "q")	
	temp2 = temp1.replace("--.. ", "z")
	temp1 = temp2.replace("-.-- ", "y")	
	temp2 = temp1.replace("-.-. ", "c")	
	temp1 = temp2.replace("-..- ", "x")
	temp2 = temp1.replace("-... ", "b")
	temp1 = temp2.replace("--- ", "o")
	temp2 = temp1.replace("--. ", "g")
	temp1 = temp2.replace("-.- ", "k")	
	temp2 = temp1.replace("-.. ", "d")
	temp1 = temp2.replace(".-- ", "w")	
	temp2 = temp1.replace(".-. ", "r")	
	temp1 = temp2.replace("..- ", "u")
	temp2 = temp1.replace("... ", "s")
	temp1 = temp2.replace("-- ", "m")
	temp2 = temp1.replace("-. ", "n")
	temp1 = temp2.replace('.- ', "a")
	temp2 = temp1.replace(".. ", "i")	
	temp1 = temp2.replace("- ", "t")
	temp2 = temp1.replace(". ", "e")
	temp1 = temp2.replace("/ ", " ")
	temp2 = temp1.replace("@", ".")
	temp1 = temp2.replace("$", "/")
	clearText = temp1
	time.sleep(.5)
	input("Decryption completed. Press enter to continue. ")
	print("")
	print("Decrypted message:", color.BOLD+clearText+color.END)
	input("Press enter to continue. ")
	print("")
	menuopts()
def menuopts():
	time.sleep(.5)
	print("Main Menu: ")
	print("")
	time.sleep(.25)
	print("	1-Encrypt a message")
	print("")
	time.sleep(.25)
	print("	2-Decrypt a message")
	print("")
	time.sleep(.25)
	print("	3-Exit the program ")
	print("")
	time.sleep(.5)
	task1 = input("Your selection: ")
	input("Press enter to continue. ")
	reloop = True
	print("")
	while reloop == True:
		if task1 == "1":
			encrypt()
			reloop = False
		elif task1 == "2":
			decrypt()
			reloop = False
		elif task1 == "3":
			exit()
		else:
			task1 = input("Please try again with either 1, 2, or 3. ")
print("\n")
time.sleep(1)
print("\n****************************************->")
print("*  Welcome to Lee's                      *")
print("*       __  __                           *")
print("*      |  \/  | ___  _ __ ___  ___       *")
print("*      | |\/| |/ _ \| '__/ __|/ _ \      *")
print("*      | |  | | (_) | |  \__ \  __/      *")
print("*      |_|  |_|\___/|_|  |___/\___|      *")
print("*                          Code Program  *")
print("******************************************\n")
print("")
print("This program is designed for International Morse. It only converts unaccented latin letters (lowercase output), spaces, numbers, and basic punctuation.")
input("Press enter to continue. ")
menuopts()