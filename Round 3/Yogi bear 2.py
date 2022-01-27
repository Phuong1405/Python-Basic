"""
The lyrics of the Yogi Bear song contain so many repetitions
that implementing it requires, in addition to the printing of the verse,
another function for printing a correct amount of repetitions of
the bear's name.

Implement a function called repeat_name, which repeats printing the bear's name
as many times as the caller of the function wants to.
The function takes 2 parameters: first the name of the name of the bear
(for example "Yogi" or "Boo Boo") and second the amount of repetitions
(an integer, for example 3). For example
the function call repeat_name("Yogi", 3) prints the fourth, fifth,
and sixth lines of the first verse,
which is a little section of the whole song.

After this, implement the function verse that has to work with
the given main function.
The function verse calls the function repeat_name.

The whole program, including 3 functions (main, verse and repeat_name),
prints 3 verses of the song lyrics as follows:

I know someone you don't know
Yogi, Yogi
I know someone you don't know
Yogi, Yogi Bear
Yogi, Yogi Bear
Yogi, Yogi Bear
I know someone you don't know
Yogi, Yogi Bear

Yogi has a best friend too
Boo Boo, Boo Boo
Yogi has a best friend too
Boo Boo, Boo Boo Bear
Boo Boo, Boo Boo Bear
Boo Boo, Boo Boo Bear
Yogi has a best friend too
Boo Boo, Boo Boo Bear

Yogi has a sweet girlfriend
Cindy, Cindy
Yogi has a sweet girlfriend
Cindy, Cindy Bear
Cindy, Cindy Bear
Cindy, Cindy Bear
Yogi has a sweet girlfriend
Cindy, Cindy Bear


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
