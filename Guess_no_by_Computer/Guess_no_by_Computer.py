import random
def guess(x):
    low = 1
    high = x
    attempts = 0
    feedback = ''
    while feedback != 'c':
        attempts += 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number {guess} correctly in {attempts} attempts :)')


guess(x = int(input('Enter the Maximum Limit: ')))