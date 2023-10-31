#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = 'and is 0'
b = 'and is less than 6 and not 0'
c = 'and is greater than 5'
if number < 0:
    print('Last digit of', -number, 'is', -(number % 10), b)
else:
    if number % n == 0:
        print('Last digit of', number, 'is', number % 10, a)
    elif number % n < 6:
        print('Last digit of', number, 'is', number % 10, b)
    else:
        print('Last digit of', number, 'is', number % 10, c)
