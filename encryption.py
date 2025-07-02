# encryption program
import random
import string

# use the string method to bring in different characters
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print (f"chars: {chars}")
# print (f"key  : {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

# iterate over each letter in our plain_text
for letter in plain_text:
    # get the letter in the plain_text
    index = chars.index(letter)
    # match it with the encryption letters and add it to the cipher_text
    cipher_text += key[index]

print (f"Original Message: {plain_text}")
print (f"Encrypted Message: {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

# iterate over each letter in our cipher_text
for letter in cipher_text:
    # get the letter in the cipher_text
    index = key.index(letter)
    # match it with the plain_text letters and add it to the plain_text
    plain_text += chars[index]

print (f"Original Message: {cipher_text}")
print (f"Encrypted Message: {plain_text}")