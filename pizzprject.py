print('Welcome to Pizza hunt dilivery place your order below:\n')

bill = 0

pizza = input('What size of pizza do you like: S, M, L: ').lower()

if pizza == 's' or pizza == 'm' or pizza == 'l':
    add_pepperoni = input('Do you want to add pepperoni? "Y"/"N": ').lower()
    if add_pepperoni == 'y' or add_pepperoni == 'n':
        extra_cheese = input('would you like to add some extra cheese? "Y"/"N": ').lower()
        if extra_cheese == 'y' or extra_cheese == 'n':
            if pizza == "s":
                bill = 400
            elif pizza == "m":
                bill = 600
            elif pizza == "l":
                bill = 1000
            if add_pepperoni == "y":
                if pizza == "s":
                    bill += 50
                else:
                    bill += 100
            if extra_cheese == "y":
                if pizza == "s":
                    bill += 50
                else:
                    bill += 100
            print(f"Your final bill is {bill} AFN")
        else:
            print('Wrong input please try again!')

    else:
        print('Wrong input please try again!')

else:
    print('Wrong input please try again!')



