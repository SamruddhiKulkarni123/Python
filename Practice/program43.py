# Accept number from user and display its factors

def DisplayFactors(iNo):
    iCnt = 0

    for iCnt in range(1,(iNo//2)+1):
        if(iNo % iCnt == 0):
            print(iCnt)

def main():
    iValue = 0
    
    print("Enter number : ")
    iValue = int(input())

    DisplayFactors(iValue)


if __name__ == "__main__":
    main()

# Time complexity : O(n/2)
# where n >= 0