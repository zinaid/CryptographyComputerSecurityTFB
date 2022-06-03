from des import DesKey
key0 = DesKey(b"some key")                  # DES
key1 = DesKey(b"a key for TRIPLE")          # 3DES
key2 = DesKey(b"a 24-byte key for TRIPLE")  # 3DES
key3 = DesKey(b"1234567812345678REAL_KEY")  # DES

key0.is_single()  # -> True
key1.is_triple()  # -> True
key2.is_single()  # -> False
key3.is_triple()  # -> False

print(key0.encrypt(b"any long message"))

print(key0.decrypt(b"%\xd1KU\x8b_A\xa6", padding=True))