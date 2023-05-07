import pyperclip

def main():
    msg = 'Python is really fun.'
    key = 7
    ciphertext = encryptMessage(msg, key)

    # sign | is called a pipe sign and is used to distinquish blank spaces at the end
    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

def encryptMessage(msg, key):
    # Each string in ciphertext represents a column in a net
    ciphertext = [''] * key # Here we create a list of 8 empty strings
    # Now we loop through for loop in range of 0-7
    for col in range(key):
        pointer = col
        # move through loop while pinter doesn't cross a message length (this case 30)
        while pointer < len(msg):
        # put character in the place of a pointer in message at the end of the looped column in cipher list
            ciphertext[col] += msg[pointer]
            # move pointer for a value of a key (first iteration in while loop is 0, then 8,16,24)
            # pomakni pointer za vrijednost kljuca (dakle prva iteracija u while loop je 0, 8, 16, 24)
            pointer += key
# Combining elements of a list into a string
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()