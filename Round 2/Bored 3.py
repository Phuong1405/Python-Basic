"""
Combine the previously implemented programs to create a program that asks
the user if they're bored until they are, and additionally requires them to
answer with the letter "y", "Y", "n" or "N",
ie. asks the user for the answer repeatedly until receiving a valid input.

Bored? (y/n) o
Incorrect entry.
Bored? (y/n) z
Incorrect entry.
Bored? (y/n) m
Incorrect entry.
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) f
Incorrect entry.
Bored? (y/n) j
Incorrect entry.
Bored? (y/n) y
Well, let's stop this, then.
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) y
Well, let's stop this, then.
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
