"""
Player 1, enter your choice (R/P/S): P
Player 2, enter your choice (R/P/S): S
Player 2 won!
Player 1, enter your choice (R/P/S): P
Player 2, enter your choice (R/P/S): R
Player 1 won!
Player 1, enter your choice (R/P/S): R
Player 2, enter your choice (R/P/S): S
Player 1 won!
Player 1, enter your choice (R/P/S): S
Player 2, enter your choice (R/P/S): S
It's a tie!
"""

def main():
    Person1 = str(input("Player 1, enter your choice (R/P/S): "))
    Person2 = str(input("Player 2, enter your choice (R/P/S): "))

    if Person1 == Person2:
        print("It's a tie!")

    elif Person1 == "R" and Person2 == "P":
        print("Player 2 won!")
    elif Person1 == "P" and Person2 == "R":
        print("Player 1 won!")
    elif Person1 == "R" and Person2 == "S":
        print("Player 1 won!")
    elif Person1 == "S" and Person2 == "R":
        print("Player 2 won!")
    elif Person1 == "P" and Person2 == "S":
        print("Player 2 won!")
    elif Person1 == "S" and Person2 == "P":
        print("Player 1 won!")




if __name__ == '__main__':
    main()
