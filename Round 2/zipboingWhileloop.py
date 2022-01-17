"""
      In the game Zip Boing players sit in a ring and call numbers in turns.
      The first player says 1, the next one 2 and so forth.
      The game is called Zip Boing because every time the next number is divisible
      by 3 the player has to say "zip" and
      every time the number is divisible by 7 the player has to say "boing".
      Also, if the umber is divisible by both the numbers,
      the player should say "zip boing".

Implement a program that makes a cheat sheet for as many numbers as
the player wants. T
he program should first ask how many numbers the cheat sheet should include and
then print them in correct order (with all the zips, boings and zip boings).


How many numbers would you like to have? 10
1
2
zip
4
5
zip
boing
8
zip
10
        """

def main():

        question = int(input("How many numbers would you like to have? "))
        num = 1
        while num <= question:
                if num % 3 == 0 and num % 7 == 0:
                        print("zip boing")
                        num = num + 1
                elif num % 3 == 0:
                        print("zip")
                        num = num + 1
                elif num % 7 == 0:
                        print("boing")
                        num = num + 1
                else:
                        print(num)
                        num = num + 1  # this will get executed every loop


if __name__ == "__main__":
        main()
