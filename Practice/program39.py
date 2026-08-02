# check whether number is divisible by 3 and 5

def CheckDivisible(iNo):

    if((iNo % 3 == 0) & (iNo % 5 == 0)):
        return True

    else:
        return False

def main():

    iValue = 0
    bRet = False

    iValue = int(input("Enter number : "))
    
    bRet = CheckDivisible(iValue)

    if(bRet == True):
        print("Number is divisible by 3 and 5")

    else:
        print("Number is not divisible by 3 and 5")


if __name__ == "__main__":
    main()