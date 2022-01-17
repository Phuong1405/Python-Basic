"""
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) y
Well, let's stop this, then.

Bored? (y/n) y
Well, let's stop this, then.
        
        
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
