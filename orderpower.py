import random
import Arts
words = ["Apple", "House", "Dog"]
# index_number = random.randint(0, len(words) - 1)
random_word = random.choice(words).lower()
print(random_word)
blank_word = []
for x in range(len(random_word)):
    blank_word.append('_')
# print(blank_word)
y = ''
for x in blank_word:
    y += f'{x} '
print(y)
# the user default lives are 6
user_lives = 0
game_process = True
while game_process:
    if '_' in blank_word:
        user_input = input('Guess the word: ').lower()
        if user_input in blank_word:
            print(f'You have already guessed letter "{user_input}" Please try another one!')
        for x in range(len(random_word)):
            if user_input == random_word[x]:
                blank_word[x] = user_input
    else:
        game_process = False
        print('You win')
    if user_input not in random_word:
        if user_lives != 5:
            user_lives += 1
        else:
            game_process = False
            print(f'You lose the currect word was "{random_word}"!')
    y = ''
    for x in blank_word:
        y += f'{x} '
    print(y)

