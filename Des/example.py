from des import DesKey

def checkKey(key):
    key_len = len(key)
    if key_len in [8, 16, 24]:
        return True
    else:
        print("Error: Key length must be 8, 16, or 24 bytes.")
        return False

def checkPlain(plain):
    if len(plain) % 8 == 0:
        return True
    else:
        print("Error: Plain text length must be divisible by 8.")
        return False

def encrypt(plain, key):

    if not checkKey(key):
        return
    if not checkPlain(plain):
        return

    # NAPRAVI DES 3DES KLJUC
    des_key = DesKey(key)

    # ENKRIPCIJA
    cipher = des_key.encrypt(plain)
    decrypted = des_key.decrypt(cipher)

    print("Encrypted text:", cipher)
    print("Decrypted text:", decrypted)
    return cipher

def main():
    with open("Des/plain.txt", "rb") as f:
        plain = f.read()

    with open("Des/key.txt", "rb") as f:
        key = f.read()

    encrypt(plain, key)

if __name__ =="__main__":
    main()