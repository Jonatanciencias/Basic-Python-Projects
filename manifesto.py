# Python program to create a MadLibs-style manifesto for a healthy and fulfilling life

'''
Instructions:
- Create a class named ShortManifesto.
    - create a method named get_user_input that takes five parameters: adjective, verb, noun, place, and feeling.
    - cretae a method named create_manifesto that uses the collected inputs to create a short manifesto with f-string formatting.
- Create a class named app.
    - create a constructor that calls the run_program method.
    - create a method named run_program that collects user inputs and creates an instance of the ShortManifesto class.
- Run the app.
'''

class ShortManifesto:
    # Method to get user input and store it in instance variables
    def get_user_input(self, adjective, verb, noun, place, feeling):
        self.__adjective = adjective
        self.__verb = verb
        self.__noun = noun
        self.__place = place
        self.__feeling = feeling

    # Method to create the short manifesto using the collected inputs
    def create_manifesto(self):
        # Create the short manifesto string using f-string formatting
        
        manifesto = f"""
        To live a truly {self.__adjective} life, one must {self.__verb} every day and find joy in simple things. 
        Cherish your {self.__noun} and always make time for loved ones. 
        Remember, a peaceful mind begins with a peaceful {self.__place}. 
        Embrace each moment and stay {self.__feeling} in every situation.
        """
        # Print the short manifesto
        print("-"*50)
        print(manifesto)
        print("-"*50)

class app:
    # CONSTRUCTOR
    def __init__(self):
        self.run_program()
    
    # Method to run the program
    def run_program(self):
        print("Welcome to the Short Healthy Living Manifesto Generator!")
        print("-"*30)

        # Collect user inputs
        print("Describe what life should be like.")
        adjective = input("Enter an adjective: ")
        print("Action that one must do every day.")
        verb = input("Enter a verb: ")
        print("Something to be valued or treasured.")
        noun = input("Enter a noun: ")
        print("A place that should be peaceful.")
        place = input("Enter a place: ")
        print("An emotional state that should be maintained.")
        feeling = input("Enter a feeling: ")

        # Create an instance of the ShortManifesto class
        new_manifesto = ShortManifesto()

        # Pass the collected inputs to the instance
        new_manifesto.get_user_input(adjective, verb, noun, place, feeling)

        # Create and print the short manifesto
        new_manifesto.create_manifesto()

# Run the app
app()