"""
        Create a program that prints the dates for all the Fridays in 2014.
        In 2014, the first Friday was 3.1.
        """

def main():
    def main():
        day_number = 0
        for month in range(1, 13):
            # print month
            for day in range(1, 32):
                if month == 2 and day <= 28:
                    # if friday:
                    if day_number % 7 == 2:
                        print(f"{day}.{month}.")
                    day_number += 1
                elif month in {4, 6, 9, 11} and day <= 30:
                    # if friday:
                    if day_number % 7 == 2:
                        print(f"{day}.{month}.")
                    day_number += 1
                elif month in {1, 3, 5, 7, 8, 10, 12}:
                    if day_number % 7 == 2:
                        # if friday:
                        print(f"{day}.{month}.")
                    day_number += 1

    # 1 + 2 * 3
    #
    if __name__ == "__main__":
        main()



if __name__ == "__main__":
    main()
