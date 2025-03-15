import random
def guess(x):
    random_n = random.randint(1, x)
    guess = 0
    while guess != random_n:
        guess= int(input(f'Pick a number between 1 and {x} '
                         f'\n'))
        if guess > random_n:
            print('Too high !! Guess again ')
        elif guess < random_n:
            print('Too low !! Guess again ')
    print(f"You guess correctly !!! \n {guess} is the correct number")

guess(10)