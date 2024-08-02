import random

alphabits = "ABCDEFGHIJKLMNOPQRSTUVWSYZ abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "~!@#$%^&*_+><?/\()"

print('>>>>>Welcome to password Generator<<<<<')

alphabits_amount = int(input('How many alphabits do you want? '))
numbers_amount = int(input('How many numbers do you want? '))
symbols_amount = int(input('How many symboles do you want? '))

password = ""

for x in range(alphabits_amount):
    random_char = random.choice(alphabits)
    password += random_char

for x in range(numbers_amount):
    random_char = random.choice(numbers)
    password += random_char
for x in range(symbols_amount):
    random_char = random.choice(symbols)
    password += random_char

print(f'Your new password generated is: {password}')