'''
- Import random module
- Create a class called GuessTheNumber
  - Create a constructor that takes an upper limit as a parameter
  - Create a method called guess that generates a random number between 1 and the upper limit
  - Create a while loop that runs until the user guesses the number
    - Ask the user to type their guess    
- Create a class to run the game
  - Instanciate the GuessTheNumber class with an upper limit of 100
  - Instantiate the guess method to start the game
- Create an instance of the Game class 
- instanceiate run method to start the game
'''
import random

class GuessTheNumber:
    def __init__(self, upper_limit: int) -> None:
        # Initialize the upper limit for the random number
        self.__upper_limit = upper_limit

    def guess(self):
        # Initialize the guess variable
        guess = 0
        # Generate a random number between 1 and upper_limit
        random_number = random.randint(1, self.__upper_limit)

        # Loop until the correct number is guessed
        while guess != random_number:
            try:
                # Get the user's guess and convert it to an integer
                guess = int(input('Please type your guess: '))
                if guess < random_number:
                    print('Too low!')
                elif guess > random_number:
                    print('Too high!')
            except ValueError:
                # Handle the case where the user input is not a valid integer
                print("Invalid input. Please enter a number.")
        
        # Print congratulations message when the correct number is guessed
        print(f'Congratulations! You guessed the number {random_number}!')

class Game:
    def run(self):
        # Print welcome messages
        print('='*30)
        print('Welcome to Guess The Number!')
        print('I am thinking of a number between 1 and 100')
        print('Can you guess what it is?')
        print('='*30)
        
        # Create an instance of GuessTheNumber with upper_limit 100
        guess_the_number = GuessTheNumber(100)
        # Start the guessing game
        guess_the_number.guess()

# Create an instance of Game and run it
new_game = Game()
new_game.run()
