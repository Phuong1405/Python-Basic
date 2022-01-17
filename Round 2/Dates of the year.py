"""
Create a program that prints all the dates of a year which is not leap year:
1.1.
2.1.
3.1.
4.1.
5.1.
...
31.1.
1.2.
2.2.
3.2.
...
28.2.
1.3.
...
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
