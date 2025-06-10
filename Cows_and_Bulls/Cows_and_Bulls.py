import random

def generate_number():
    number = ''
    while len(number) < 3:
        digit = str(random.randint(1, 9))  # Avoid 0
        if digit not in number:
            number += digit
    return number

def get_cows_and_bulls(guess, number):
    cows = 0
    bulls = 0
    for i in range(3):
        if guess[i] == number[i]:
            bulls += 1
        elif guess[i] in number:
            cows += 1
    return cows, bulls

def main():
    number = generate_number()
    attempts = 0

    print("Welcome to Cows and Bulls!")
    print("Guess the 3-digit number:")

    while True:
        guess = input().strip()
        if len(guess) != 3 or not guess.isdigit() or '0' in guess or len(set(guess)) != 3:
            print("Invalid input. Enter a 3-digit number with unique digits (1-9):")
            continue

        attempts += 1
        cows, bulls = get_cows_and_bulls(guess, number)

        if bulls == 3:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break
        else:
            print(f"Cows: {cows}, Bulls: {bulls}")
            print("Try again:")

main()
