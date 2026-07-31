# Take name , age and marks from user and display it on screen

def main():
    name = []
    age = 0
    marks = 0.0

    print("Enter your name : ")
    name = input()

    print("Enter your age : ")
    age = int(input())

    print("Enter your marks : ")
    marks= float(input())

    print("Name : ",name);
    print("Age : ",age);
    print("Marks : ",marks)



if __name__ == "__main__":
    main()