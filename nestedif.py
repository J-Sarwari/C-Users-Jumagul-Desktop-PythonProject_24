print('Welcome to kabul city park please enter your information below:\n')

height = float(input('Please enter your height in meters: '))
age = int(input('Please enter your age: '))

ticket = 0


if height < 2:
    if age > 18:
        if age > 60:
            print('you are not allowed!')
        else:
            ticket = 200
            print('200 AFN')
    elif age >= 10:
        ticket = 150
        print('150 AFN')
    else:
        ticket = 100
        print('100 AFN')

    user_input = input('Do you want to take a photo? "Y"/"N" ')
    if user_input == "Y":
        ticket += 50
        print(f'you final ticket price is {ticket} AFN')
    else:
        print(f'your ticket price is {ticket} AFN')

else:
    print('Dear customer you are not allowed!')
