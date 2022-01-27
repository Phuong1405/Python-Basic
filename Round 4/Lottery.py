"""
       In other words, write it inside triple quotes like this
       and place it right in the beginning of your program file.
       Initial comment should explain who wrote the program and
       what does it do.
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