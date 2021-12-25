def main():

    cost = int(input("Purchase price: "))
    paid = int(input("Paid amount of money: "))

    if cost < paid:
        refund = paid - cost
        print("Offer change:")



    #1, 2, 5, 10

        if refund >= 10:
            print(refund//10, "ten-euro notes")
            refund = refund - refund // 10 * 10

        if refund >= 5:
            print(refund//5, "five-euro notes")
            refund = refund - refund // 5 * 5

        if refund >= 2:
            print(refund//2, "two-euro coins")
            refund = refund - refund // 2 * 2

        if refund >= 1:
            print(refund, "one-euro coins")

    else:
        print("No change")

if __name__ == '__main__':
    main()

