"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""
class Player:


# TODO:
# a) Implement the class Player here.
    def __init__(self, name, points = 0, count=0, counter=0):
        self.__name = name
        self.__points = points
        self.__count = count
        self.__counter = counter
    def get_name(self):
        """get the name of each player"""
        return self.__name
    def get_points(self):
        """get the point of individual player"""
        return self.__points
    def has_won(self):
        """tell whether player has won
        return: Boolean"""
        if self.__points == 50:
            return True
        else:
            return False
    def add_points(self, points):
        self.__points += points
        self.__count += 1
        if points > 0:
            self.__counter += 1
        if self.__points > 50:
            print(f"{self.__name} gets penalty points!")
            self.__points = 25
        if self.__points >= 40 and self.__points <= 49:
            needpoint = 50 - self.__points
            print(f"{self.__name} needs only {needpoint} points. It's better to avoid knocking down the pins with higher points.")

    def average(self):
        avg = self.__points/self.__count
        return avg

    def percentage(self):
        if self.__count == 0:
            return 0.0
        else:
            time = f"{(self.__counter/self.__count)*100:.1f}"
            return time


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)


        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        if in_turn.average() < pts:
            print(f"Cheers {in_turn.get_name()}!")
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage", player1.percentage()) # TODO: d)
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage", player2.percentage())  # TODO: d)
        print("")

        throw += 1


if __name__ == "__main__":
    main()
