# REVERSE CIPHER
message = 'This is an application that shows reverse cipher'
translated = '' # Here we save cipher text
i = len(message) - 1 # Calculate length of a message

while i >= 0: # Here we loop through each position backwards and save in translated variable new char
   translated = translated + message[i]
   i = i - 1

print("Cipher text is : ", translated)
