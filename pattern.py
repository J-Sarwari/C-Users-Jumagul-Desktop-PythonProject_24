a = ['◽️', '◽️', '◽️', '◽️']
b = ['◽️', '◽️', '◽️', '◽️']
c = ['◽️', '◽️', '◽️', '◽️']

main_list = [a, b, c]

print(f'{a}\n{b}\n{c}')


user_input = input('Please find the treasure: ')

x = int(user_input[0])
y = int(user_input[1])

main_list[x - 1][y - 1] = '*'

print(f"{a}\n{b}\n{c}")
