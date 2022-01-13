"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.
        """

def main():

        question = int(input("How many numbers would you like to have? "))
        num = 1
        while num <= question:
                if num % 3 == 0 and num % 7 == 0:
                        print("zip boing")
                        num = num + 1
                elif num % 3 == 0:
                        print("zip")
                        num = num + 1
                elif num % 7 == 0:
                        print("boing")
                        num = num + 1
                else:
                        print(num)
                        num = num + 1  # this will get executed every loop


if __name__ == "__main__":
        main()