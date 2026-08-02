# check whether number is divisible by 3 and 5

def CheckDivisible(iNo):

    if((iNo % 3 == 0) & (iNo % 5 == 0)):
        print("Number is divisible by 3 and 5\n")

    else:
        print("Number is not divisible by 3 and 5\n")

def main():

    iValue = 0

    iValue = int(input("Enter number : "))
    
    CheckDivisible(iValue)


if __name__ == "__main__":
    main()