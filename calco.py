

def temp_calculator(temp, direction):
    Fahrenheit = (temp * 9/5) + 32
    Celsius = (temp - 32) * 5/9

    if direction == 'c':
        return f"{temp}°C is equal to {Fahrenheit}°F"
    else:
        return f"{temp}°F is equal to {round(Celsius, 2)}°C"




x = temp_calculator(temp=float(input('Please enter the temp value: ')), direction=input('Please enter the temp unit (C/F): ').lower())

print(x)