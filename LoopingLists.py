#task1
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Iterate over the genres list using enumerate() to get the index and value
for index, genre in enumerate(genres, start=1):
    print(f"Track {index}: This track is {genre}.")

#task2
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Initialize the track counter
track_number = 1

# Initialize the index
index = 0

# Loop until 'Hip-hop' is played
while index < len(genres):
    genre = genres[index]
    print(f"Track {track_number}: This track is {genre}.")
    track_number += 1
    if genre == 'Hip-hop':
        print("Stopping the loop because Hip-hop is played.")
        break
    index += 1

#task3
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Loop through the genres list by index
for index in range(len(genres)):
    genre = genres[index]
    
    # Check if the genre is suitable for the light show
    if genre == 'Classical':
        continue  # Skip the 'Classical' genre
    
    # Print the track number and a message for each genre
    track_number = index + 1
    print(f"Track {track_number}: The light show is ready for {genre}.")
