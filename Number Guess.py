#Thomas Anstis
#Number guessing game
import random

# Set attempts to 0 initially
attempts = 0

# Ask the player if they want to play
play = input("Do you want to play my number guessing game? (yes/no) ")

if play.lower() == "yes":
    # Generate the random number once before the game starts
    number = random.randint(1, 100)
    
    while True:
        try:
            # Ask the player for a guess
            attempt = int(input("Please choose a number from 1 to 100: "))
        except ValueError:
            # Handle invalid input (non-numeric)
            print("Please enter a valid number.")
            continue
        
        # Increment the number of attempts
        attempts += 1

        # Provide feedback to the player
        if attempt < number:
            print("Too low. Try again.")
        elif attempt > number:
            print("Too high. Try again.")
        else:
            # The player guessed correctly
            print(f"Congratulations! You have guessed the number in {attempts} attempts.")
            break  # Exit the loop when the game ends

else:
    print("Maybe next time!")  # If the player doesn't want to play

        
    
    
    
    
    
    
    
    
    
