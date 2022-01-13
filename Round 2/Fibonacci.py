"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.
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