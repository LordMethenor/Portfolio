print("Welcome to the Atbash Cipher program")
input("press enter to contiue")

print("")
clear_text = input("Type in your message: ")
clear_text = clear_text.lower()
print("")

input("Press enter to continue")
cipher_text = clear_text.replace("a","Z")
cipher_text = cipher_text.replace("b","Y")
cipher_text = cipher_text.replace("c","X")
cipher_text = cipher_text.replace("d","W")
cipher_text = cipher_text.replace("e","V")
cipher_text = cipher_text.replace("f","U")
cipher_text = cipher_text.replace("g","T")
cipher_text = cipher_text.replace("h","S")
cipher_text = cipher_text.replace("i","R")
cipher_text = cipher_text.replace("j","Q")
cipher_text = cipher_text.replace("k","P")
cipher_text = cipher_text.replace("l","O")
cipher_text = cipher_text.replace("m","N")
cipher_text = cipher_text.replace("z","A")
cipher_text = cipher_text.replace("y","B")
cipher_text = cipher_text.replace("x","C")
cipher_text = cipher_text.replace("w","D")
cipher_text = cipher_text.replace("v","E")
cipher_text = cipher_text.replace("u","F")
cipher_text = cipher_text.replace("t","G")
cipher_text = cipher_text.replace("s","H")
cipher_text = cipher_text.replace("r","I")
cipher_text = cipher_text.replace("q","J")
cipher_text = cipher_text.replace("p","K")
cipher_text = cipher_text.replace("o","L")
cipher_text = cipher_text.replace("n","M")

print(cipher_text)
