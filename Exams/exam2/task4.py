import onetimepad
import random, sys

def OneTimePadEncrypt(plain):
    cipher = onetimepad.encrypt(plain, 'random')
    return cipher

def OneTimePadDecrypt(cipher):
    plain = onetimepad.decrypt(cipher, 'random')
    return plain

def main():
    random.seed(42)

    for i in range(20): # 20 tests
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(1, 10)

        message = list(message)
        random.shuffle(message)
        message = ''.join(message) 

        cipher = OneTimePadEncrypt(message)
        decrypted = OneTimePadDecrypt(cipher)
        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        if(message == decrypted):
            print("Working")
        else:
            print("Not Working")
            sys.exit()

    print('Transposition cipher test passed.')

if __name__ == "__main__":
    main()