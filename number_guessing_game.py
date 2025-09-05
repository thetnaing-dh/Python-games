import random
#Generate a random number
number_to_guess = random.randint(1,100)
#Loop 
while True:
    #Ask the user to make a guess
    #Get an integer number catch error
    try:
        guess_number = int(input ('Guess the number between 1 and 100: '))
            #If number < guess
            #   Print too low
        if guess_number < number_to_guess:
            print('Too low!')  
            #If number > guess
            #   Print too high
        elif guess_number > number_to_guess:
            print('Too high!')
            #Else
            #   Print well done
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        #If not a valid number
        #   Print an error
        print('Please enter a valid number')


  
    
   