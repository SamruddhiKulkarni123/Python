# Check whether number is evven or odd

def CheckEvenOdd(iNo):
    iRemainder = 0
    iRemainder = iNo % 2
    return iRemainder
    

def main():
    iValue = 0
    iRet = 0

    print("Enter number to check whether it is even or odd :")
    iValue = int(input())   

    iRet = CheckEvenOdd(iValue)

    if(iRet == 0):
        print("Number is even")
    else:
        print("Number is odd")



if __name__ == "__main__":
    main()