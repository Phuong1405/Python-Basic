"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.
        """
def main():

    while True:
        a = input("Bored? (y/n) ")
        if a== "n":
            continue
        elif a== "y":
            print("Well, let's stop this, then.")
            break

if __name__ == "__main__":
        main()