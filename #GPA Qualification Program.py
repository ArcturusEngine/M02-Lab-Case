#GPA Qualification Program
#A program written by Bryce Bland
#This is a program that will take the input of several students to determine what their GPA earns them.
x = 0 #x is a counter to make sure that 5 names will be entered
while x != 5:
    l_name = input("What is your last name?: ")
        if l_name == "ZZZ": #This is to terminate the program if the name is ZZZ
        break
    f_name = input("What is your first name?: ")

    gpa = float(input(f"Hi {name}, what is your GPA?: "))
    if gpa <= 3.25:
        print(f"I'm sorry {name}, you have not made it to honor roll or the Dean's list")
    elif 3.5 > gpa >= 3.25:
        print(f"Congratulations, {name}! You're on the honor roll!")
    elif gpa >= 3.5:
        print(f"Incredible job {name}, You've made it to the Dean's list!")
    x += 1
