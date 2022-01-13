"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.
        """
def main():
        question = int(input("How many numbers would you like to have? "))
        for num in range(1, question + 1):
                if num % 21 == 0:
                        print("zip boing")
                elif num % 3 == 0:
                        print("zip")
                elif num % 7 == 0:
                        print("boing")
                else:
                        print(num)


if __name__ == "__main__":
        main()