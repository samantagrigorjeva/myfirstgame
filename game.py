import random

turns = ['Rock','Paper','Scissors']

while(True):
    
    human_turn = input('enter your turn: ')
    computer_turn = random.choice(turns)
    
    if human_turn =='exit':
        print('bye bye')
        break

    print(f'human: {human_turn} vs. Computer: {computer_turn}')

    if human_turn == computer_turn:
        print('Draw!')
    elif human_turn == 'Rock' and computer_turn == 'Scissors':
        print('Human wins!')
    elif human_turn == 'Paper' and computer_turn == 'Rock':
        print('Human wins!')
    elif human_turn == 'Scissors' and computer_turn == 'Paper':
        print('Human wins!')
    elif human_turn == 'rock' and computer_turn == 'Scissors':
        print('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'Rock':
        print('Human wins!')
    elif human_turn == 'scissors' and computer_turn == 'Paper':
        print('Human wins!')
    else:
        print('Computer wins!')
