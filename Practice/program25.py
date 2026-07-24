# print "Jay Ganesh" on screen as per user demand

def Display(iNo):

    iCnt = 0

    # Updater
    if(iNo < 0):
        iNo = -iNo

    for iCnt in range(1,iNo+1):
        print("Jay Ganesh...")

def main():
    iValue = 0

    iValue = int(input("Enter value :"))

    Display(iValue)


if __name__ == "__main__":
    main()