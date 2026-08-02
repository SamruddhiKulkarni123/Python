# check whether number is divisible by 3 and 5

def main():

    iValue = 0

    print("Enter number : ")
    iValue = int(input())

    if((iValue % 3 == 0) & (iValue % 5 == 0)):
        print("Number is divisible by 3 and 5\n")

    else:
        print("Number is not divisible by 3 and 5\n")
    


if __name__ == "__main__":
    main()