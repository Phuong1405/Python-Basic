"""
COMP.CS.100 Programming 1
Code template for tanssipelit assigment.

Read Python's documentation concerning dicts.
After this, implement the next program using the method values().

In dancing games, the player's score is given as a percentage of the song's maximum score.
In the attached file template, there exists a predefined dict.
The dict contains pairs that include the song's name and a percent value for the song.

Implement the function calculate_average, which takes the dict as a parameter and calculates the average from the song percentage values,
which is also the return value of the function.

An example of how the function operates when tested on a Python console:

>>> calculate_average(SONG_RESULT)
83.81700000000001
"""

SONG_RESULT = {"Bubble dancer": 93.4, "The Game": 92.03, "Vertex": 75.3,
               "Lemmings on the Run": 86.2, "Da Roots": 96.02,
               "Charlene": 75.3, "Disconnected": 86.3, "Fly away": 87.32,
               "Hybrid": 63.9, "My favourite game": 89.45, "Oasis": 59.5,
               "Remember December": 96.3, "The beginning": 90.45,
               "Tribal Style": 87.45, "Why Me": 97.38, "Xuxa": 63.84,
               "Zodiac": 83.43, "Queen of Light": 75.12, "Mouth": 98.34,
               "Pandemonium": 79.31}

def calculate_average(SONG_RESULT):
    """Function to start checking each song"""
    #convert_values = list(PRICES.values())
    values_price = list(SONG_RESULT.values())
    sum_price = sum(values_price)
    result = sum_price/len(values_price)
    return result


if __name__ == "__calculate_average__":
    calculate_average()
