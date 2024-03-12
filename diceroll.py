import random
# instructions: run the code and choose the number of the dice you want to roll


def dice():
    what_dice = int(input('How many faces your dice have?: '))
    # choose a random number between 1 and the number chosen by the player
    roll = random.randint(1, what_dice)
    print(f'You have rolled a {roll}')
    again1 = input('Do you want to roll the same dice again? (yes or no): ')
    # roll the same dice again
    while again1.lower() == 'yes':
        roll = random.randint(1, what_dice)
        print(f'You have rolled a {roll}')
        again1 = input('Do you want to roll the same dice again? (yes or no): ')
    # call function to ask if player want to choose another dice
    if again1.lower() == 'no':
        again2()
    else:
        print('Please answer with yes or no only')


def again2():
    other_dice = input('Do you want to roll another dice? (yes or no): ')
    if other_dice.lower() == 'yes':
        dice()
    elif other_dice.lower() == 'no':
        print('Thank you for playing')
    else:
        print('Please answer with yes or no only')
        again2()


dice()
