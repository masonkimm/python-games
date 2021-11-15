import random
from colorama import Fore


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'{Fore.GREEN}Guess a number between 1 and {x}: '))
        if guess < random_number:
            print(f'{Fore.RED} Sorry, try again..Your guess was too low')
        elif guess > random_number:
            print(f'{Fore.RED} Sorry, try again...Your guess was too high')

    print(f'{Fore.YELLOW}Correct! The number was {random_number}')


guess(10)
