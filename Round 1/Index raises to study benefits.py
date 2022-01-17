"""Write a program that asks how much study benefits the user receives and calculates how a 1,17 percent index raise affects the benefits. The program prints the following:

Enter the amount of the study benefits: 335.32
If the index raise is 1.17 percent, the study benefit,
after a raise, would be 339.243244 euros

Let’s be optimistic about the future and add another index raise to our program. Now the program prints the following:

Enter the amount of the study benefits: 335.32
If the index raise is 1.17 percent, the study benefit,
after a raise, would be 339.243244 euros
and if there was another index raise, the study
benefits would be as much as 343.2123899548 euros

"""

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
