# *****************LIBRARY IMPORT*****************************
import random

# ***************CLUE*****************************************
print('Here is a clue for your!!')


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


secret_number = random.randint(0, 100)
is_prime(secret_number)

if is_prime(secret_number):
    print('CLUE: Secret number is a PRIME Number!!')
else:
    if secret_number % 2 == 0:
        print('CLUE: Secret number is an EVEN Number!!')
    else:
        print('CLUE: Secret number is an ODD Number!!')

# *****************GUESS COUNT********************************

for guess_taken in range(0, 5):
    print('My guess number', guess_taken + 1, ': ')

    guess = int(input())
    if guess < secret_number:
        print('Your guess is too low!')

    elif guess > secret_number:
        print('Your guess is so high!!')

    elif guess == secret_number:
        print('WoW!!..Your Guessed it right!')
        print('You won the game!')
        break
    else:
        print('Did not match!! One more try please ...!!')


# **********************NO MORE OPTION*************************
else:
    print('You do not have any guess option!')
    print('You Lost!')
    print('The secret number was : ', secret_number)

# **********************GAME OVER******************************
print('Game Over!')

# **************************DONE*******************************
