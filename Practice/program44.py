# Accept number from user and display sum of its factors

def SumFactors(iNo):
    iCnt = 0
    iSum = 0

    for iCnt in range(1,(iNo//2)+1):
        if(iNo % iCnt == 0):
            iSum = iSum + iCnt

    print("Sum of factors is : ",iSum)

def main():
    iValue = 0
    
    print("Enter number : ")
    iValue = int(input())

    SumFactors(iValue)


if __name__ == "__main__":
    main()

# Time complexity : O(n/2)
# where n >= 0