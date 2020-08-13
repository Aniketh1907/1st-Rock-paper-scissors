import utils
# import the random module
import random

print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')
player_count = 0
computer_count = 0
while player_count <5:
    print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
    player_hand = int(input('Please enter a number (0-2): '))

    if utils.validate(player_hand):
        # Assign a random number between 0 and 2 to computer_hand using randint
        computer_hand = random.randint(0,2)
    
        utils.print_hand(player_hand, player_name)
        utils.print_hand(computer_hand, 'Computer')

        result = utils.judge(player_hand, computer_hand)
        if result == 'Win':
            player_count+=1
        elif result == 'Lose':
            computer_count+=1

        print('Result: ' + result)
    else:
        print('Please enter a valid number')
if player_count>=5:
    print(player_name+' won')
elif computer_count>=5:
    print('computer won')
    
