'''

'''

# Python program to create a MadLibs-style manifesto for a healthy and fulfilling life

def get_user_input(prompt):
    return input(prompt)

def create_manifesto():
    # Collect user inputs
    adjective1 = get_user_input("Enter an adjective: ")
    adjective2 = get_user_input("Enter another adjective: ")
    noun1 = get_user_input("Enter a noun: ")
    noun2 = get_user_input("Enter another noun: ")
    verb1 = get_user_input("Enter a verb: ")
    verb2 = get_user_input("Enter another verb: ")
    food1 = get_user_input("Enter a type of food: ")
    activity1 = get_user_input("Enter an activity: ")
    activity2 = get_user_input("Enter another activity: ")
    place = get_user_input("Enter a place: ")
    feeling = get_user_input("Enter a feeling: ")

    # Create the manifesto
    manifesto = f"""
    Manifesto for a {adjective1} and {adjective2} Life

    1. Balanced Diet
       Make sure to include a variety of {food1} in your diet to stay {adjective1} and energized.

    2. Regular Exercise
       Engage in {activity1} and {activity2} regularly to keep your {noun1} strong and your mind sharp.

    3. Mental Health
       It's important to {verb1} time for yourself. Practice mindfulness and ensure you {verb2} your stress effectively.

    4. Sleep Hygiene
       Good sleep is crucial. Create a {adjective2} bedtime routine to improve your sleep quality.

    5. Hydration
       Drink plenty of water to stay {feeling}. Carry a {noun2} with you to ensure you drink enough throughout the day.

    6. Preventive Healthcare
       Regular check-ups at your local {place} can help prevent health issues before they start.

    7. Healthy Relationships
       Build {adjective1} relationships with those around you. Support and be supported.

    8. Work-Life Balance
       Balance your {noun1} responsibilities with your personal life to reduce stress and increase {feeling}.

    9. Healthy Habits
       Develop {adjective2} habits like regular exercise, balanced eating, and avoiding harmful behaviors.

    10. Positive Mindset
        Cultivate a positive mindset by practicing gratitude and setting achievable goals.

    11. Community Involvement
        Get involved in your community through {activity2}, social groups, and local activities.

    12. Personal Growth
        Pursue continuous personal growth through {activity1}, education, and self-reflection.

    13. Financial Health
        Manage your finances effectively by budgeting, saving, and investing wisely.

    14. Environmental Awareness
        Live sustainably and understand the impact of your actions on the {place}.

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

    Remember, a healthy life is a {adjective1} life!
    """

    # Print the manifesto
    print(manifesto)

# Run the program
create_manifesto()
