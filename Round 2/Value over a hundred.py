"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.
        """
def main():
    number = int(input("Choose a number: "))
    multiplier = 1
    calculated_value = 0
    while calculated_value < 100:
        calculated_value = multiplier * number
        print(multiplier, "*", number, "=", calculated_value)
        multiplier += 1 #multiplier = multiplier +1
if __name__ == "__main__":
        main()