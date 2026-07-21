# Calculation of Ticket price on the basis of Age

def main():

    iValue = 0

    print("Enter age to calculate ticket price : ")
    iValue = int(input())

    if((iValue >= 0) & (iValue <= 5)):
        print("Your ticket price is 0")

    elif((iValue >= 6) & (iValue <= 18)):
        print("Your ticket price is 500")

    elif((iValue >= 19) & (iValue <= 50)):
        print("Your ticket price is 900")

    else:
        print("Your ticket price is 400")


if __name__ == "__main__":
    main()