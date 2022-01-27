"""
COMP.CS.101 Programming 1
Code template for the hottest hit song Yogi Bear
"""

def repeat_name(name, repetition):
    """starting the name and the repetition of the name"""
    for i in range (0,repetition):
        print(f"{name}, {name}"" ""Bear")

def verse(lyrics, name):
    """the first verse, which is a little section of the whole song
            name and the line of the song """
    print(lyrics)
    print(f"{name}, {name}")
    print(lyrics)
    repeat_name(name,3)
    print(lyrics)
    repeat_name(name,1)

def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()
