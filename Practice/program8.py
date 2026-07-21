# Check whether number is evven or odd

def main():
    iValue = 0
    iRemainder = 0
    
    print("Enter number to check whether it is even or odd :")
    iValue = int(input())

    iRemainder = iValue % 2

    if(iRemainder == 0):
        print("Number is even")

    else:
        print("Number is odd")

if __name__ == "__main__":
    main()