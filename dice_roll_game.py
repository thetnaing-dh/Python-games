import random
#Loop
while True:
    #Ask: roll the dice?
    choice = input("Roll the dice? (y/n): ").lower()
    #If user enters yes
    if choice =='y':
    #   Generate two random numbers
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
    #   Print Item
        print(f'({dice1}, {dice2}, {dice3})')
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
