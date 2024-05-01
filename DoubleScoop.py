#task1
import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through the days of the week
for day in days_of_week:
    print(f"Mood tracker for {day}:")
    # Loop through the times of the day
    for time in ["Morning", "Afternoon", "Evening"]:
        # Randomly select a mood from the list
        random_mood = random.choice(moods)
        # Print the mood for the current time
        print(f"{time}: {random_mood}")
    print()  # Add a blank line for better readability between days
