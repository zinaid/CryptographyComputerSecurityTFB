from des import DesKey
import os


def checkKey(key):
    if(len(key) in (8, 16, 24)):
        return True
    else:
        return False

def checkPlain(plain):
    if(len(plain) % 8 == 0):
        return True
    else:
        return False

def encrypt(plain, key):
    key = DesKey(bytes(key, 'utf-8'))
    encrypted = key.encrypt(bytes(plain, 'utf-8'))
    return encrypted

def main():

    try:
        file = open("key.txt", "r")

        key = file.read()

    finally:
        file.close()

    try:
        file = open("plain.txt", "r")

        plain = file.read()

    finally:
        file.close()

    if(checkKey(key) and checkPlain(plain)):
        print("Encrypted text: ")
        print(encrypt(plain, key))
    else:
        print("Error in plain text or a key")

if __name__ == "__main__":
    main()