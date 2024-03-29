"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.
    :param: filename
    :return: series_catalog

    TODO: comment the parameter and the return value.
    """

    # TODO initialize a new data structure

    dictionary = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            # TODO add the name and genres data to the data structure
            if name not in dictionary:
               dictionary[name]=genres

        file.close()
        # TODO return the data structure
        return dictionary

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    # TODO print the genres
    listing = []
    for genres in genre_data.values():
        #print(genres)
        for i in genres:
            if i not in listing:
                listing.append(i)
                listing.sort()
    real_genres = ", ".join(listing)
    print(f"Available genres are: {real_genres}")

    while True:
        genre = input("> ")
        if genre == "exit":
            return

        # TODO print the series belonging to a genre.
        #sorting the dictionary by passing the dict to a value
        #then looping the value
        sorting = genre_data.items()
        sorted_genre = sorted(sorting)
        for key , value in sorted_genre:
            if genre in value:
                print(key)

if __name__ == "__main__":
    main()


