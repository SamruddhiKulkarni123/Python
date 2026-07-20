# perform addition of two numbers

def main():
    iValue1 = 0
    iValue2 = 0
    iAns = 0

    print("Enter first number : ")
    iValue1 = int(input())

    print("Enter second number : ")
    iValue2 = int(input())

    iAns = iValue1 + iValue2
    print("Additon is : ",iAns)

if __name__ == "__main__":
    main()