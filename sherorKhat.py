import image
import  random

coin = random.randint(0, 1)
if coin == 0:
    print('Heads\n')
    print(image.heads)
else:
    print('Tails')
    print(image.tails)
