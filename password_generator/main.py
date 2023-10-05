import random
import string

print("Welcome to the Password Generator!")

chars = string.ascii_letters+string.digits+string.punctuation

passwordNum = input("Enter the number of passwords you'd like to generate: ")
passwordNum = int(passwordNum)

passwordLength = input("Please enter your desired password length: ")
passwordLength = int(passwordLength)

print("Generating your passwords below...\n")

for pwd in range(passwordNum):
    passwords = ''
    for c in range(passwordLength):
        passwords += random.choice(chars)
    print(passwords)
