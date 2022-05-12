# 09 - INSTRUKCJE WARUNKOWE
light = input('What\'s the light color? ( red, green, yellow) :  ')

if light == 'red':
    print('Wait!')

elif light == 'yellow':
    print('Get ready')

else:
    print('GO')

# nie korzystać w przyzawiłych funkcjach

# 10 - PĘTLE WHILE I FOR

print("Second part of lesson \n self printing numbers from 1 to 10")

number = 1

from time import sleep

while number < 10:
    sleep(1)
    print(number)
    number += 1
