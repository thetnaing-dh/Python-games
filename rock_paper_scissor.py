import random

ROCK = 'r'
SCISSOR = 's'
PAPER = 'p'

#Dictionary  for emojis
emojis = {ROCK:'🪨', SCISSOR:'✂️', PAPER:'📃'}

#Arrays of Dictionary keys
choices = tuple(emojis.keys())

#Function for user choice
def get_user_choice():
    while True:
    #Ask the user to make a choice
        user_choice = input('Rock, Paper or Scissor? (r,p,s): ').lower()
        #If choice is valid
        if user_choice in choices:
            return user_choice                    
        else:
            #  Print an error
            print('Please make a valid choice!')
            continue

def display_choices(user_choice, computer_choice):
        #Print emojis using format string and dictionary
        print(f'You choose {emojis[user_choice]}')
        print(f'Computer choose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
        #Determine the winner
        if user_choice == computer_choice:
            print('Tie!')

        elif ((user_choice == ROCK and computer_choice == SCISSOR) or
            (user_choice == SCISSOR and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
            print('You Win!')
        else:
            print('You Lose!')

def play_game():
    while True :
            user_choice = get_user_choice()
            #Let the computer to make a choice
            computer_choice = random.choice(choices)
            
            display_choices(user_choice, computer_choice)

            determine_winner(user_choice, computer_choice)

            #Ask the user if they want to continue
            should_continue = input('Are you want to continue? (y/n): ').lower()
            #If not
            #   Terminate
            if should_continue == 'n':
            #   Print thank you message
                print('Thank you for playing!')
                break

play_game()
