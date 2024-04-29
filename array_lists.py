# Creating Album class
class Album:
    """Album class with 3 attributes and an str method to
    be able to print them out in the required format """
    def __init__(self, album_name, number_of_song, album_artist):
        self.album_name = album_name
        self.number_of_song = int(number_of_song)
        self.album_artist = album_artist

    # Here is the str method with the required format
    def __str__(self):
        return f'({self.album_name}, {self.album_artist}, {self.number_of_song})'


# A list containing the albums
albums1 = [Album("Rocking album", 32, "Britney Pears"),
           Album("Too much", 22, "Cortney Kox"),
           Album("Flew away", 17, "Jimmy Dumpet"),
           Album("Once more", 28, "Kyle Mitove"),
           Album("Take it", 11, "Coby Walker")]

# Printing the albums
for i in range(len(albums1)):
    print(albums1[i])

# Sort the list "albums"
albums1.sort(key=lambda album: album.number_of_song)

# Adding an empty line for better readability and printing the list
print('\n Sorted list: ')
for i in range(len(albums1)):
    print(albums1[i])

# Swap the position of the first 2 elements
albums1[0], albums1[1] = albums1[1], albums1[0]

# Adding an empty line for better readability
print('\n Swapped elements: ')
for i in range(len(albums1)):
    print(albums1[i])

# Creating the 2nd list
albums2 = [Album("Fun", 18, "Richie Dixxon"),
           Album("Riot", 21, "Marylin Tenson"),
           Album("Back up", 23, "Selin Spion"),
           Album("Try harder", 29, "John Spartan"),
           Album("In love", 13, "Acton Pusher")]

# Adding an empty line for better readability
print('\n 2nd list: ')
for i in range(len(albums2)):
    print(albums2[i])

# Copying all elements from album1 to album2
albums2.extend(albums1)

# Adding extra 2 elements to albums2
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

# Sorting albums2 alphabetically
albums2.sort(key=lambda album: album.album_name)

# Adding a new line and printing the index of the album name
print('\n Index of the album: ')
for i in range(len(albums2)):
    if albums2[i].album_name == "Dark Side of the Moon":
        print(i)
