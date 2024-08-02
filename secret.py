from hot import logo
import replit

clear()

print(logo)

bids = {}

def result():
    heighest_bid = 0
    winner = ""
    for x in bids:
        values = bids[x]
        if values > heighest_bid:
            heighest_bid = values
            winner = x
    print(f'The winner of the auction is Mr/Ms {winner} with the heighest bit of ${heighest_bid}')

process = True
while process:
    user_name = input('Please enter your name:')
    user_bid = int(input('Please enter your biders? yes or no: '))
    bids[user_name] = user_bid
    go_again = input('are there any other biders? yes or no:')
    if go_again == 'no':
        result()
        process = False
    elif go_again == 'yes':
        clear()
    else:
        print('Wrong input please type yes or no')
