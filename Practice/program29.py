# print 0 to N on screen

def Display(iNo):

    iCnt = 0

    # Filter
    if(iNo < 0):
        print("Invalid input")
        return

    for iCnt in range(0,iNo+1):
        print(iCnt)

def main():
    iValue = 0

    iValue = int(input("Enter value :"))

    Display(iValue)


if __name__ == "__main__":
    main()