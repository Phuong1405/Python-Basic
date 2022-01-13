"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.y
        Initial comment should explain who wrote the program and
        what does it do.
        """
def main():
    answer = input("Bored? (y/n) ")
    while answer != "y":
        while answer != "n":
            print("Incorrect entry.")
            break
        answer = input("Bored? (y/n) ")
    print("Well, let's stop this, then.")

if __name__ == "__main__":
        main()