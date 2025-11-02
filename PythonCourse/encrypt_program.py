import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars: {chars}")
print(f"key:   {key}")

#Encrypt
plain_text = input("Enter a message to encrypt: ")
cyper_text = ""

for letter in plain_text:
    idx = chars.index(letter)
    cyper_text += key[idx]

print(f"Original_message: {plain_text}")
print(f"Encrypted_message: {cyper_text}")


