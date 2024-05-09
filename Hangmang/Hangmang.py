# 1_ List of names
# 2_ Select one name random
# 3_ Get user 
# 4_ Chek ---> show feed back
# 5_ Guess > 0 ---> win/loss   

import random

names = ['Mahdi','Ali','Hossien','Saman','Abed','Behzad','Javad']

selected_name = random.choice(names).lower()


guess_count = len(selected_name)
guess_list = ['-'] * len(selected_name)
current_guess = ''.join(guess_list)
print(current_guess)


while guess_count > 0:
    guess_char = input('Enter a char: \n')

    if guess_char.isalpha():
        if guess_char in selected_name:
            if guess_char in guess_list:
                print('you have guessed before try new character')
            else:
                for idx , char in enumerate(selected_name):
                    if char == guess_char:
                        guess_list[idx] = guess_char
                current_guess = ''.join(guess_list)
                print(f'Perfect --->{current_guess}')

                if not'-' in guess_list:
                    print('You won')
                    break
        else:
            guess_count -=1
            print(f'Wrong! ---> remained guesse:{guess_count}')
    else:
        print('Please enter a valid character')