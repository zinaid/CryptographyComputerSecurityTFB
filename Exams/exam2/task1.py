# Defining function
def encrypt(plain_text,key):
    result = "" # Variable for saving the result
    for i in range(len(plain_text)): # Looping through entire text
        char = plain_text[i]
        # chr function has all ascii signs
        # ord function returns a position of a character
        # encryption of uppercase letters (65-91)
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        # encryption of lowercase letters (97-123)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

def main():
    plain_text = "This is a good day"
    key = 4
    print ("Plain text : " + plain_text)
    print ("Shift : " + str(key))
    print ("Cipher text: " + encrypt(plain_text,key))

if __name__ == '__main__':
    main()