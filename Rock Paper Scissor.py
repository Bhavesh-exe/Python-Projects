import random

player = input("Enter your choice: ").lower()
computer = random.choice(['rock', 'paper', 'scissor'])

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
    
print(f'You chose {player} and computer chose {computer}')