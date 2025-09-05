import random
import time

user_dices_sum = 0
computer_dices_sum = 0

#Loop
while True:
    #Ask: roll the dice?
    choice = input("Roll the dices? (y/n): ").lower()
    #If user enters yes
    if choice =='y':
    #   Generate three random numbers
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
    #   Sum User dices
        user_dices_sum = dice1 + dice2 + dice3
    #   Print Item
        print(f'Your dices are :({dice1}, {dice2}, {dice3})')

    # Computer Roll dices
        symbols = ['.', '..', '...', '....', '.....']
        i = 0
        for i in range(5):
            i = (i + 1) % len(symbols)
            print('\r\033 [Computer roll the dices: %s' % symbols[i], flush=True, end='')
            time.sleep(0.2)
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
    #   Sum Computer dices
        computer_dices_sum = dice1 + dice2 + dice3
    #   Print Item
        print(f'\rComputer dices are :({dice1}, {dice2}, {dice3})')

    #   Determine Winner
        if user_dices_sum == computer_dices_sum:
            print('Tie!')
        elif user_dices_sum > computer_dices_sum:
            print('You Win!')
        else:
            print('You Lose!')

    #If user enter no
    elif choice =='n':
    #   Print thank you message
        print('Thank you for playing!')
    #   Terminate
        break
    #Else
    else:
    #   Print invalid choice
        print('Invalid choice!')
