# EXAM EXAMPLE 1

1. Using programming language Python encrypt this sentence: <b>"Today we have an exam in course Computer Systems Security."</b> using <b>Reverse Cipher Algorithm</b>.
   
2.  Using programming language Python implement the next scenario. User from keyboard chooses an option "E" or "D", encryption or decryption. After that, program asks him to enter plain text for encryption, that is cipher text for decryption. Over the entered text, program performs encryption, that is decryption with <b>OneTimePad algorithm</b>. Result is written in terminal, as well it is saved in the following files "encrypted.txt" or "decrypted.txt".

3.  Using programming language Python perform an encryption of the following sentence: <b>"ROT13 algorithm is not reliable."</b> using <b>ROT13 algorithm</b> and function maketrans over the next symbols:
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm

1. Using programming language Python and <b>base64 algorithm</b> implement the next scenario. User enters text for encryption and saves it inside a variable msg. That variable is forwarded to encrypt method, and the result that is returned with that method is forwarded to decrypt method. Perform comparation between the variable that is entered using keyboard and the result of the decrypt method. If those two are the same, write a message in terminal "Result of decryption and entry message are the same.". Create two methods: encrypt(msg) and decrypt(msg) that are called through main() method.