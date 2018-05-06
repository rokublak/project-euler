'''

Project Euler - Problem 3 (Short way)
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import time

start_time = time.time()

number = 600851475143
potentialfactor = 2 # If it started as one, while loop will go on forver.

while (potentialfactor * potentialfactor) < number:
    while number % potentialfactor == 0:
        number = number / potentialfactor
    potentialfactor += 1
    
print(number)

print('--- %s seconds ---' % (round((time.time() - start_time), 10)))