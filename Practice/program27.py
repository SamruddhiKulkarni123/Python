# print "Jay Ganesh" with index value

def Display(iNo):

    iCnt = 0

    # Filter
    if(iNo < 0):
        print("Invalid input")
        return

    for iCnt in range(1,iNo+1):
        print(iCnt," Jay Ganesh...")

def main():
    iValue = 0

    iValue = int(input("Enter value :"))

    Display(iValue)


if __name__ == "__main__":
    main()