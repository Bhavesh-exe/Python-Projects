import random

player = input("Enter your choice: ").lower()
computer = random.choice(['rock', 'paper', 'scissor'])

print(f'You choose {player} and \nComputer choose {computer}')

if player == computer:
    print('Its a tie!')
    
elif player == 'rock' and computer == 'scissor':
    print('You win!')

elif player == 'paper' and computer == 'rock':
    print('You win!')

elif player == 'scissor' and computer == 'paper':
    print('You win!')

else:
    print('You lose!')
