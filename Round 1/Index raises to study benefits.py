def main():
    amount = float(input("Enter the amount of the study benefits: "))

    amount = float(amount)

    index_raise = 1.17

    afteroneraise = float(index_raise * amount / 100 + float(amount))

    anotherraise = float(afteroneraise * 1.17 / 100 + afteroneraise)

    print("If the index raise is 1.17 percent, the study benefit,")
    print("after a raise, would be", afteroneraise, "euros ")
    print("and if there was another index raise, the study ")
    print("benefits would be as much as", anotherraise, "euros")




if __name__ == '__main__':
    main()