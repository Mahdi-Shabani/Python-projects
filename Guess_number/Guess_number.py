# 1_ user input ---> low and high
# 2_ random ---> [a,b]
# 3_ loop ---> condition ---> guess_counts=5 ---> feedback

import random 
try:
    low = int(input('Enter lower bound :\n'))
    high = int(input('Enter high bound:\n'))
except:
    print('Please enter a valid number:')

r = random.randint(low,high)

guess_count=5

while guess_count>0:
    try:
        new_guess_str = input(f'remained guess : {guess_count} enter your next guess: \n')
        new_guess = int(new_guess_str)

        if r ==new_guess:
            print('Greate your guess is correct')
            break
        elif r > new_guess:
            print('Your guess id lower than selected number')
        else:
            print('Your guess is high than selected number')

        guess_count -=1
    except:
        print('Please  enter a valid number') 