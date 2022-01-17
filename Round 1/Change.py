"""
Purchase price: 12
Paid amount of money: 50
Offer change:
3 ten-euro notes
1 five-euro notes
1 two-euro coins
1 one-euro coins

Purchase price: 11
Paid amount of money: 50
Offer change:
3 ten-euro notes
1 five-euro notes
2 two-euro coins

Purchase price: 9
Paid amount of money: 20
Offer change:
1 ten-euro notes
1 one-euro coins

Purchase price: 12
Paid amount of money: 12
No change
Purchase price: 23
Paid amount of money: 15
No change"""


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

