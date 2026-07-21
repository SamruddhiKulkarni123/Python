# Calculation of Ticket price on the basis of Age

def CalculateTicketPrice(iAge):

    # Input updater
    if(iAge < 0):
        iAge = -iAge

    if((iAge >= 0) & (iAge <= 5)):
        return 0

    elif((iAge >= 6) & (iAge <= 18)):
        return 500

    elif((iAge >= 19) & (iAge <= 50)):
        return 900

    else:
        return 400

def main():

    iValue = 0
    iRet = 0

    print("Enter age to calculate ticket price : ")
    iValue = int(input())

    iRet = CalculateTicketPrice(iValue)

    print("Your Ticket price is : ",iRet)


if __name__ == "__main__":
    main()