# Defining function
def encrypt(text,s):
    result = "" # Variable for saving the result
    for i in range(len(text)): # Looping through entire text
        char = text[i]
        # chr function has all ascii signs
        # ord function returns a position of a character
        # encryption of uppercase letters (65-91)
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # encryption of lowercase letters (97-123)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

# Checking function
text = "CAESARCIPHERALGORITHM"
s = 64
print ("Plain text : " + text)
print ("Shift : " + str(s))
print ("Cipher text: " + encrypt(text,s))