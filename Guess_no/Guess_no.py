import random

def guess(x):
    random_no = random.randint(1 ,x)
    guess = 0
    attempts = 0
    while guess != random_no:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        attempts += 1

        if guess < random_no:
            print('Sorry, Guess again. Too Low.')

        elif guess > random_no: 
            print('Sorry, Guess again. Too High.')

    print(f'Yay, Congrats. You have guessed the number {random_no} correctly in {attempts} attempts :)')

guess(x = int(input('Enter the Maximum Limit: ')))