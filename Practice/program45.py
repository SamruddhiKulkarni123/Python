# Accept number from user and display sum of its factors

def SumFactors(iNo):
    iCnt = 0
    iSum = 0

    for iCnt in range(1,(iNo//2)+1):
        if(iNo % iCnt == 0):
            iSum = iSum + iCnt

    return iSum

def main():
    iValue = 0
    iRet = 0
    
    print("Enter number : ")
    iValue = int(input())

    iRet = SumFactors(iValue)

    print("Sum of factors is : ",iRet)


if __name__ == "__main__":
    main()

# Time complexity : O(n/2)
# where n >= 0