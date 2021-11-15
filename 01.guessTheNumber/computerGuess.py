import random
from colorama import Fore


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(
            f'{Fore.GREEN}Is {guess} too high (H), too low (L), or correct (C): ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'{Fore.YELLOW}Correct! The number was {guess}')


computer_guess(1000)
