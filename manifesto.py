'''

'''

# Python program to create a MadLibs-style manifesto for a healthy and fulfilling life

class Manifesto:
  # Method to get user input and store it in instance variables
  def get_user_input(self, adjective1, adjective2, noun1, noun2, verb1, verb2, food1, activity1, activity2,  place, feeling):
      self.__adjective1 = adjective1
      self.__adjective2 = adjective2
      self.__noun1 = noun1
      self.__noun2 = noun2
      self.__verb1 = verb1
      self.__verb2 = verb2
      self.__food1 = food1
      self.__activity1 = activity1
      self.__activity2 = activity2
      self.__place = place
      self.__feeling = feeling
  def create_manifesto(self):
      
      # Create the manifesto
      manifesto = f"""
      Manifesto for a {self.__adjective1} and {self.__adjective2} Life

      1. Balanced Diet
        Make sure to include a variety of {self.__food1} in your diet to stay {self.__adjective1} and energized.

      2. Regular Exercise
        Engage in {self.__activity1} and {self.__activity2} regularly to keep your {self.__noun1} strong and your mind sharp.

      3. Mental Health
        It's important to {self.__verb1} time for yourself. Practice mindfulness and ensure you {self.__verb2} your stress effectively.

      4. Sleep Hygiene
        Good sleep is crucial. Create a {self.__adjective2} bedtime routine to improve your sleep quality.

      5. Hydration
        Drink plenty of water to stay {self.__feeling}. Carry a {self.__noun2} with you to ensure you drink enough throughout the day.

      6. Preventive Healthcare
        Regular check-ups at your local {self.__place} can help prevent health issues before they start.

      7. Healthy Relationships
        Build {self.__adjective1} relationships with those around you. Support and be supported.

      8. Work-Life Balance
        Balance your {self.__noun1} responsibilities with your personal life to reduce stress and increase {self.__feeling}.

      9. Healthy Habits
        Develop {self.__adjective2} habits like regular exercise, balanced eating, and avoiding harmful behaviors.

      10. Positive Mindset
          Cultivate a positive mindset by practicing gratitude and setting achievable goals.

      11. Community Involvement
          Get involved in your community through {self.__activity2}, social groups, and local activities.

      12. Personal Growth
          Pursue continuous personal growth through {self.__activity1}, education, and self-reflection.

      13. Financial Health
          Manage your finances effectively by budgeting, saving, and investing wisely.

      14. Environmental Awareness
          Live sustainably and understand the impact of your actions on the {self.__place}.

      15. Time Management
          Manage your time effectively to increase productivity and reduce stress.

      16. Self-Care
          Prioritize self-care routines to maintain your physical, emotional, and mental health.

      17. Nutrition Education
          Make informed food choices by understanding nutrition labels and portion sizes.

      18. Mind-Body Connection
          Explore the connection between mental and physical health through practices like yoga and mindfulness.

      19. Resilience Building
          Develop resilience to cope with life's challenges and bounce back from setbacks.

      20. Goal Setting
          Set and achieve personal and professional goals for a sense of accomplishment and direction.

      Remember, a healthy life is a {self.__adjective1} life!
      """

      # Print the manifesto
      print(manifesto) 

      # Function to run the program and collect user inputs
  def run_program():
    print("Welcome to the Healthy Living Manifesto Generator!") 
       
    # Collect user inputs
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    food1 = input("Enter a type of food: ")
    activity1 = input("Enter an activity: ")
    activity2 = input("Enter another activity: ")
    place = input("Enter a place: ")
    feeling = input("Enter a feeling: ")

    # Create an instance of the Manifesto class
    new_manifesto = Manifesto()

    # Pass the collected inputs to the instance
    new_manifesto.get_user_input(adjective1, adjective2, noun1, noun2, verb1, verb2, food1, activity1, activity2, place, feeling)

    # Pass the collected inputs to the instance
    new_manifesto

  # Run the program
  run_program()
