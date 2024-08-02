weight = int(input('please enter your weight in KG:'))
height = int(input('please ebter your height in meters:'))

bmi = weight / (height ** 2)

x = height ** 2
y = weight / x

if bmi < 18.5:
    print(f'{round(bmi, 2)} >>> im sorry to inform you are underweight!')
elif bmi < 25:
    print(f'{round(bmi, 2)} >>> good news you ahve a normal weight!')
elif bmi <= 30:
    print(f'{round(bmi, 2)} >>> you are over weight!')
else:
    print(f'{round(bmi, 2)} >>> please go and see the doctor!')


