# Check whether number is evven or odd

def CheckEvenOdd(iNo):
    iRemainder = 0
    iRemainder = iNo % 2
    
    if(iRemainder == 0):
        return True
    else:
        return False

def main():
    iValue = 0
    iRet = False

    print("Enter number to check whether it is even or odd :")
    iValue = int(input())   

    iRet = CheckEvenOdd(iValue)

    if(iRet == True):
        print("Number is even")
    else:
        print("Number is odd")



if __name__ == "__main__":
    main()