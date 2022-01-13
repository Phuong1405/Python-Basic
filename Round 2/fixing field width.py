"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.
        """

def main():
        for i in range(1, 11):
            for j in range(1, 11):
               print("",f"{i * j:=3}", end="")
            print("")


if __name__ == "__main__":
    main()


