# Take name , age and marks from user and display it on screen

def Display(name,age,marks):

    print("Name : ",name);
    print("Age : ",age);
    print("Marks : ",marks)

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

    Display(name,age,marks)



if __name__ == "__main__":
    main()