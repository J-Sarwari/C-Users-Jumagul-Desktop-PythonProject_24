print('Welcome to Pizza dilivery place your order bello:\n')


pizza = input('What size of pizza do you like: S,M, L ').lower()
add_pepperoni = input('Do you want to add pepperoni? "Y"/"N":').lower()
extra_cheese = input('Would you like to add some extra cheese/ "Y"/"N": ').lower()

bill = 0

if pizza == "S":
    bill = 400
elif pizza == "M":
    bill = 600
elif pizza == "L":
    bill = 1000
else:
    print('wrong input please try again!')

if add_pepperoni == "Y":
    if pizza == "S":
        bill +=50
    else:
        bill +=100
if extra_cheese == "Y":
    if pizza == "S":
        bill += 50
    else: bill += 100
print(f" your final bill is {bill} AFN")
