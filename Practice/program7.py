# perform addition of two numbers

def Addition(iNo1, iNo2):

    return iNo1 + iNo2


def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    iValue1 = int(input("Enter first number : "))

    iValue2 = int(input("Enter second number : "))

    iRet = Addition(iValue1, iValue2)
    print("Additon is : ",iRet)

if __name__ == "__main__":
    main()