#task1
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Create a slice of genres from the second to the fourth track
sublist_genres = genres[1:4]

# Loop through the sublist of genres and print them
for genre in sublist_genres:
    print(genre)

#task2
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# List comprehension to create a new list with "Music" appended to each genre
genres_with_music = [genre + " Music" for genre in genres]

# Print the new list
print(genres_with_music)

#task3
# Loop using range() to print out a countdown
for i in range(10, 0, -1):
    print(i)

# Print the message after the countdown
print("The beat drops now!")
