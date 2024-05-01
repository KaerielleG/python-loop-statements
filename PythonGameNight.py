#task1
import random

# List of items
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Select a random item from the list
selected_item = random.choice(items)

# Prompt the user to guess
guess = input("Guess which item was selected from the list: ")

# Check if the guess is correct
if guess.lower() == selected_item:
    print("Congratulations! You guessed correctly.")
else:
    print(f"Sorry, the selected item was '{selected_item}'. Try again next time.")
