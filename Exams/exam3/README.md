# EXAM 3

# TRANSPOSITION ALGORITHM - 35

Implement transposition algorithm with a shif 7. Plain message that is encrypted is "Danas je kolokvij.". Print the encryption time in seconds.

# ONETIMEPAD ALGORITHM - 30

Create an automated tests script that checks the correctnes of a OneTimePad algorithm by creating 20 random messages and checking the result of the decryption with provided message. If any of the checks fails exit from the program and write "Not working", else write each message and write "Working". The tests should be recreated every time (random.seed).

# DES ALGORITHM - 35

Using Python programming language create a program that reads a plain text and a key from files named <b>plain.txt</b> and <b>key.txt</b>. That plain text and key are saved into a variables plain and key and used as a parameter in the function <b>encrypt(plain, key)</b> that uses DES algorithm. There should be a helper function named <b>checkKey(key)</b> that takes the key and checks if the key is 8, 16 or 24. Also create a helper function named <b>checkPlain(plain)</b> that checks if the plain text is divisible by 8. These helper functions are called in the function <b>encrypt(plain, key)</b>. If any of these conditions is not satisfied write some message, else do the DES encrpytion.

Tasks 2 and 3 are already inside an exam2.