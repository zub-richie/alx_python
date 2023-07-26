#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
convert = str(number)
last_digit = (convert[-1])
converbck = int(last_digit)
if converbck < 6:
     print("Last digit of " "{}" " is " "{}" " and is less than 6 and not 0".format(number, converbck))
elif converbck == 0:
    print("Last digit of " "{}" " is " "{}" " and is 0".format(number, converbck))
else:
    print("Last digit of " "{}" " is " "{}" " and is greater than 5".format(number, converbck))
