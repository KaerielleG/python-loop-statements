#task1
import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through the days of the week
for day in days_of_week:
    # Randomly select a mood from the list
    random_mood = random.choice(moods)
    
    # Print the mood for the current day
    print(f"On {day}, I am feeling {random_mood}.")
