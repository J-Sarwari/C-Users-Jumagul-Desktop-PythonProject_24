import  pepses
import random

images = [pepses.rock, pepses.paper, pepses.scissors]
names = ['Rock', 'Paper', 'Scissors']

computer_choice = random.randint(0,2)

user_choice = int(input('Please select 0 = Rock, 1 = Paper, and 2 = Scissors'))

if user_choice == 0 or user_choice == 1 or user_choice == 2:
    print(names[user_choice])
    print(images[user_choice])
    print(names[computer_choice])
    print(images[computer_choice])
    if computer_choice == user_choice:
        print('Draw')
    elif user_choice == 0 and computer_choice == 2:
        print('You Win!')
    elif user_choice == 1 and computer_choice ==0:
        print('You Win!')
    elif user_choice == 2 and computer_choice ==1:
        print('You Win')
    else:
        print('Your Lose!')
else:
    print('Wrong input please try again!')