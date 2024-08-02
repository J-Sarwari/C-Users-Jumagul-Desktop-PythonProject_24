import random
words = ['Apple', 'House', 'Dog']


random_word = random.choice(words)
print(random_word)
blank_word = []
for x in range(len(random_word)):
    blank_word.append('_')
print(blank_word)

user_input = input('Guess the word: ')

for x in range(len(random_word)):
    if user_input == random[x]:
        blank_word[x] = user_input

print(blank_word)
