"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Code template for a simplified car assignment
implementation using a class.
"""
class Player:
    """
    class Player implement a game that involves two players, where players
    aim to reach 50 points, if player has more than 50 points then it will
    be decreased to 25 points
    """
    def __init__(self, name, points=0, total_points=0, counter=0, played_round=0):
        """

        :param name: string, name of the player
        :param points: integer, point received by the particular player
        :param total_points: integer, sum of individual point received at each throw
        :param counter: integer, counts the number of throws
        :param played_round: integer, counts number of time player receive more than 0 points
        """
        self.__name = name
        self.__points = points
        self.__total_points = total_points
        self.__counter = counter
        self.__played_round = played_round

    def get_name(self):
        """
        get the name of the particular player
        :return: string, name of the player
        """
        return self.__name

    def get_points(self):
        """
        get the point of individual player
        :return: integer, point of individual player
        """
        return self.__points

    def add_points(self, points):
        """
        add point of the player on each throws
        :param points: integer, point received by player on each throw
        """
        self.__points += points
        self.__total_points += points
        self.__counter += 1
        if points > 0:
            self.__played_round += 1

        if self.__points>=40 and self.__points<=49:
            required_points = 50 - self.__points
            print(f"{self.__name} needs only {required_points} points. "
                  f"It's better to avoid knocking down the pins with higher points.")

        if self.__points > 50:
            print(f"{self.__name} gets penalty points!")
            self.__points = 25

    def get_average(self):
        """
        get average of the the total point of a player
        :return: float, total average of player
        """
        total_average = self.__total_points / self.__counter
        return total_average

    def get_accuracy(self):
        """
        accuracy how much player hit the point on each round
        :return: float, player accuracy
        """
        if self.__counter == 0:
            return 0.0
        else:
            result = f"{(self.__played_round / self.__counter)*100:.1f}"
            return result

    def has_won(self):
        """
        tell whether player has won
        :return: boolean, returns true or false
        """
        if self.__points == 50:
            return True
        else:
            return False


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

        if pts > in_turn.get_average():
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage", player1.get_accuracy())
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage", player2.get_accuracy())
        print("")

        throw += 1


if __name__ == "__main__":
    main()