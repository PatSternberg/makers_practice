from random import randint
fav_number = 77
guess_correct_firstgo = False
guess_number = 1
guess_totalnumber = 0

while guess_correct_firstgo == False:
    guess = randint(0, 100)
    if ( guess_number == 1 ) and ( guess == fav_number ):
        guess_totalnumber = guess_totalnumber + 1
        print(f'You guessed right: {fav_number}!')
        print(f'Guessed first time! After {guess_totalnumber} times')
        guess_correct_firstgo = True
    elif guess == fav_number:
        guess_totalnumber = guess_totalnumber + 1
        print(f'You guessed right: {fav_number}!')
        print(f'Guessed {guess_number} times!')
        guess_number = 1
    else:
        print(f'{guess} is wrong! Try again.')
        guess_number = guess_number + 1

