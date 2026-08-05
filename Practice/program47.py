# Accept number from user and check whether it is perfect or not

def CheckPerfect(iNo):
    iCnt = 0
    iSum = 0

    for iCnt in range(1,(iNo//2)+1):
        if(iNo % iCnt == 0):
            iSum = iSum + iCnt

        if(iSum > iNo):
            break

    if(iSum == iNo):
        return True
    else:
        return False

def main():
    iValue = 0
    bRet = False
    
    print("Enter number : ")
    iValue = int(input())

    bRet = CheckPerfect(iValue)

    if(bRet == True):
        print("Number is perfect")
    else:
        print("Number is not perfect")


if __name__ == "__main__":
    main()

# Time complexity : O(n/2)
# where n >= 0