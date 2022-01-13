"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.
        """


def main():
    for month in range (1,13):
    #print month
        for day in range(1,32):
                if month == 2 and day <=28:
                        print(f"{day}.{month}.")
                elif month in {4,6,9,11} and day <= 30:
                        print(f"{day}.{month}.")
                elif month in {1,3,5,7,8,10,12}:
                        print(f"{day}.{month}.")
 #1 + 2 * 3

if __name__ == "__main__":
        main()