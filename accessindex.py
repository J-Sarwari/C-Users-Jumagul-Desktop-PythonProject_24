import random

words = ['Apple','House', 'Dog']

random_words = random.choice(words)

print('random_word')

blank_word = []

for x in range(len(random_words)):
    blank_word.append('_')
user_input = input('Guess the Word:')

for x in random_words:
    if user_input == x:
        print('right')
else:
        print('wrong')
