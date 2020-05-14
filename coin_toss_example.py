# coin_toss_example.py
# Simple coin toss gusessing game

# random module imported as it helps to use its functions to find random numbers within given range
import random

# Main method
if __name__ == "__main__":

    guess = ''
    # Two options are provided as heads & tails are 2 sides of coin
    options = ['tails', 'heads']

    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter tails or heads:')

        # Takes input from user either heads or tails
        guess = input()

    # randint helps to find random number between given range of numbers
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    print("Toss value 0 means tails & 1 means heads")
    print("Toss value is-",toss)

    if guess == options[toss]:
        print('Your guess is correct!')
    else:
        print('Guess again!')

        # Takes input from user
        guess = input()
        if guess == options[toss]:
            print('Your guess is correct!')
        else:
            print('Your guess is not correct.It is not matching with toss value')
