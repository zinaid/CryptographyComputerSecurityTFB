import math, pyperclip

def main():
    msg = 'Tig.rtoairnoisntp hoamsl '
    key = 8
    plaintext = decryptMessage(key, msg)    
    print(plaintext + '|')
    pyperclip.copy(plaintext)

def decryptMessage(key, poruka):

    numOfColumns = math.ceil(len(poruka) / key) # getting the number of columns
    numOfRows = key # getting the number of rows
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(poruka) # number of shaded cells in the last column

    # Each string in plain text represents a column in a net
    plaintext = [''] * numOfColumns
    # variables col and row represents place of a character in a net
    col = 0
    row = 0

    # For loop moves through characters in a string
    for symbol in poruka:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()