"""
       In other words, write it inside triple quotes like this
       and place it right in the beginning of your program file.
       Initial comment should explain who wrote the program and
       what does it do.

There are all sorts of lotteries around the world.
Their typical shared feature is having a few balls drawn at random from a certain number of numbered balls.
Depending on how many of these selected balls the player (a.k.a. gambler) has guessed correctly, he or she will receive a price.
In this task, we are interested by the probabilities of the player winning the jackpot, ie. guessing all the balls correctly. In Finnish lottery, for instance, this would mean the probability of the player guessing all 7 balls correctly with only one lottery ticket.
This is a combinatorics-related problem: how many different ways are there to select 7 balls from 39 balls?
Let's assume that n is the number of balls in a lottery and p
the number of the predicted balls. In this case,
there are

Implement a program that asks the user for two input values:

the amount of lottery balls (or numbers) and
the drawn balls (or numbers).
and then prints the probability of getting a jackpot with only one coupon (1 divided with the number of different lottery lines). Additionally have the program print the following error messages:

"The number of balls must be a positive number."
"At most the total number of balls can be drawn."
The total number of balls and the number of drawn balls are always asked before checking for errors. First thing to check is whether the numbers of balls are positive. If there is an error, print an error message and terminate the program's run immediately. If both entered numbers are positive, check the numbers of the balls. An error message is also printed in this case there is an error, and the program's run is terminated.

       """

def ask_initial_values():
    """ask_initial_values starts the input and the condition"""
    total = int(input("Enter the total number of lottery balls: "))
    drawn = int(input("Enter the number of the drawn balls: "))

    if total < 1 or drawn < 1:
        return False, "The number of balls must be a positive number."
    elif drawn > total:
        return False, "At most the total number of balls can be drawn."
    else:
        return total,drawn

def permutations(n):
    """the calculation for the multiplier"""
    if n == 0:
        return 1
    else:
        result = 1
        for multiplier in range (1,n+1):
            result = result * multiplier
    return result

def combinations(n, p):
    """calculating the formula of the probability"""
    calculate = permutations(n)/(permutations(n-p)*permutations(p))
    return calculate

def print_probability(n, p):
    """print probability is for trying step"""
    result = (f"{combinations(n, p):.0f}")
    print(f"The probability of guessing all {p} balls correctly is 1/{result}")


def main():
    total_number, drawn_number = ask_initial_values()

    if not total_number:
        print(drawn_number)
    else:
        print_probability(total_number, drawn_number)

if __name__ == "__main__":
    main()
