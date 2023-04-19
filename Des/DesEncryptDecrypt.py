from des import DesKey
key0 = DesKey(b"some key")                  # DES
key1 = DesKey(b"a key for TRIPLE")          # 3DES
key2 = DesKey(b"a 24-byte key for TRIPLE")  # 3DES
key3 = DesKey(b"1234567812345678REAL_KEY")  # DES

key0.is_single()  # -> True
key1.is_triple()  # -> True
key2.is_single()  # -> False
key3.is_triple()  # -> False

encrypted = key0.encrypt(b"any long message")
encrypted_str = encrypted.hex()  # convert the bytes to a hex string for printing
print("Cipher is: " + encrypted_str)

decrypted = key0.decrypt(encrypted).decode('utf-8')
print("The decrypted string is: " + decrypted)