import random
words = ['Apple', 'Banana', 'Orange']

random_word = random.choice(words).lower()


print(random_word)

blank_word = []

for x in range(len(random.word)):
        blank_word.append('_')

print(blank_word)

game_process = True

while game_process:
    if '_' in blank_word:
        user_input = input('Guess the word: ').lower()
        for x in range(len(random_word)):
            if user_input == random_word[x]:
                blank_word[x] = user_input
    else:
        game_process = False
        print('You Win')

print(blank_word)
