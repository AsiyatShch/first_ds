# It's gonna be a guess number game

import numpy as np

number = np.random.randint(1,101) # Random number
count = 0

while True:
    count += 1
    predict_number = int(input('So your guess? '))
    
    if predict_number > number:
        print('The number is smaller!')
    
    if predict_number < number:
        print('The number is bigger!')
        
    if predict_number == number:
        print(f'Thats right! Its number {number}, you used {count} tries!')    
        break
    