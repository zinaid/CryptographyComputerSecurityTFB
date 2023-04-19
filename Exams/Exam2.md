# EXAM EXAMPLE 2

1. Using Python programming language implement <b>Caesar Cipher algorithm</b>. Create function <b>encrypt(plain_text, key)</b> that accepts a plain message: "This is a good day" and a key 4. Encrypt function is called from the main function.

Koristeći Python implementirati Cezar Cipher algoritam. Napraviti funkciju encrypt(plain_text, key) koja uzima ulaznu poruku "This is a good day" i ključ 4. Encrypt funkcija se zove iz main funkcije.
   
2. Using Python programming language create a program that reads a plain text and a key from files named <b>plain.txt</b> and <b>key.txt</b>. That plain text and key are saved into a variables plain and key and used as a parameter in the function <b>encrypt(plain, key)</b> that uses DES algorithm. There should be a helper function named <b>checkKey(key)</b> that takes the key and checks if the key is 8, 16 or 24. Also create a helper function named <b>checkPlain(plain)</b> that checks if the plain text is divisible by 8. These helper functions are called in the function <b>encrypt(plain, key)</b>. If any of these conditions is not satisfied write some message, else do the DES encrpytion.

Koristeći Python napraviti program koji čita plain tekst i ključ iz fajlova plain.txt i key.txt. Plain tekst i ključ su spremljeni u varijable plain i key i koriste se kao parametri u funkciju encrypt(plain, key) koja implementira DES algoritam. Potrebno je imati i funkcije checkKey(key) koja provjerava da li je ključ 8,16 i 24. Napraviti i funkciju checkPlain(plain) koja provjerava da li je plain djeljiv sa 8. Ove funkcije se zovu u encrypt(plain, key) i ako neki od ovih uslova nije zadovoljan ne radi se enkripcija i ispisuje odgovarajuća poruka, suprotno se radi.

3. Using Python programming language and Transposition algorithm encrypt this message: <b>"Python is really fun"</b>.

Koristeći Python i Transpozicijski algoritam enkriptovati poruku "Python is really fun". 

4. Create an automated tests script that checks the correctnes of a OneTimePad algorithm by creating 20 random messages and checking the result of the decryption with provided message. If any of the checks fails exit from the program and write "Not working", else write each message and write "Working". The tests should be recreated every time (random.seed).

Napraviti skriptu koja radi automatske testove i provjerava tačnost OneTimePad algoritma tako što pravi 20 random poruka i provjerava rezultat dekripcije sa ulaznom porukom. Ako neka provjera ne prođe ispisati "Not working" suprotno ispisati sve poruke i "Working". Testovi se moraju moći rekreirati svakim pokretanjem.