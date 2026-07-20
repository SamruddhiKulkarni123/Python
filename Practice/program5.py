# perform addition of two numbers

def Addition(iNo1, iNo2):
    iAns = 0

    iAns = iNo1 + iNo2

    return iAns

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter first number : ")
    iValue1 = int(input())

    print("Enter second number : ")
    iValue2 = int(input())

    iRet = Addition(iValue1, iValue2)
    print("Additon is : ",iRet)

if __name__ == "__main__":
    main()