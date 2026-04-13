# TASK 1. Implement both encryption and decryption for Caesar cipher

Message: "Security is important"
Key: 5

Create encrypt (text, key) i decrypt(text, key). Preserve sšaces and handle lowercase + uppercase. 

Why is Caesar cipher insecure?

# TASK 2. Hashing and passwords

Create a simple password system.

Flow:
User enters password

Hash it using SHA-256

Store hash in file

Ask user to login

Verify password by hashing again

Why not store raw passwords?
Why is SHA-256 still not ideal for passwords?

# TASK 3. AES File encryption

Encrypt and decrypt a file using AES-GCM. 

Flow:
Generate random key
Encrypt file input.txt
Save: nonce|ciphertext
Decrypt and restore original file

What happens if ciphertext is modified?
Why is AES-GCM better than plain AES?

# TASK 4. Diffie-Hellman

Simulate key exchange between Alice and Bob. Given p=23, and g=5.

Flow:
Generate private keys (random)
Compute public keys
Compute shared secret
Print both secrets and prove they match

What attack is possible here?

