print('Welcome to pizza hunt divlivery plae your order bello: \n')
def main(new_pizza, new_add_pepperoni, new_extra_chees):
    bill = 0
    if new_pizza == "s":
        bill = 400
    elif new_pizza == "m":
        bill == 600
    elif new_pizza == "1":
        bill = 1000
    else:
        print('Wrong input please tryu again!')

    if new_add_pepperoni == "y":
        if new_pizza == "s":
            bill += "50"
        else:
            bill += 100
    print(f'Your final bill is {bill} AFN')

pizza = input('What size of pizza do you like: S,M, L: ').lower()
add_pepperoni = input('Do you want to add pepperoni? "Y"/"N":').lower()
extra_cheese = input('Wold you like to add some extra cheese? "Y"/"N":').lower()


main(new_add_pepperoni=add_pepperoni, new_pizza=pizza, new_extra_chees=extra_cheese)

