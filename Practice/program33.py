# Take name , age and marks from user and display it on screen

def Display(name,age,marks):

    print("Name : ",name);
    print("Age : ",age);
    print("Marks : ",marks)

def main():

    name = input("Enter your name : ")

    age = int(input("Enter your age : "))

    marks= float(input("Enter your marks : "))

    Display(name,age,marks)



if __name__ == "__main__":
    main()