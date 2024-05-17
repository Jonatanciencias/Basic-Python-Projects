# Python program to create a MadLibs-style manifesto for a healthy and fulfilling life

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
        print(manifesto)

class app:
    # CONSTRUCTOR
    def __init__(self):
        self.run_program()
    
    # Method to run the program
    def run_program(self):
        print("Welcome to the Short Healthy Living Manifesto Generator!")
        print("-"*30)

        # Collect user inputs
        adjective = input("Enter an adjective: ")
        verb = input("Enter a verb: ")
        noun = input("Enter a noun: ")
        place = input("Enter a place: ")
        feeling = input("Enter a feeling: ")

        # Create an instance of the ShortManifesto class
        new_manifesto = ShortManifesto()

        # Pass the collected inputs to the instance
        new_manifesto.get_user_input(adjective, verb, noun, place, feeling)

        # Create and print the short manifesto
        new_manifesto.create_manifesto()

# Run the app
app()