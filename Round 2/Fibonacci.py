"""
The two first numbers of the Fibonacci sequence are ones. The numbers after them are calculated by counting together the two preceding numbers, again and again. Implement a program that prints the Fibonacci sequence for a number of times set by the user:

How many Fibonacci numbers do you want? 7
1. 1
2. 1
3. 2
4. 3
5. 5
6. 8
7. 13  
        """
def main():
    nterms = int(input("How many Fibonacci numbers do you want? "))

    # first two terms
    n1, n2 = 1, 1
    count = 0
    step = 1

    # if there is only one term, return n1
    if nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        while count < nterms:
            print(f"{step}. {n1}")
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            step += 1
if __name__ == "__main__":
        main()
