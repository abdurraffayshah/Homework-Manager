from pyfiglet import Figlet
from tabulate import tabulate
import sys
import csv
import time
from student import Student

def main():
    print(title("WELCOME TO THE HOMEWORK MANAGER"))
    checking = login()
    print(checking)
    if checking == "Successful Login":
        s_checking = students()
        print(s_checking)
        if s_checking == "Found them!":
            print(f"Would you like to know if {name} has done their homework or change their homework status?")
            user = input("Please type Y to change status and N to check their homework status: ").lower()
            if user == "n":
                print(data())
            elif user=="y":
                print(change())
    else:
        sys.exit("See you soon!")


def title(name):
    font=Figlet(font="slant")
    return font.renderText(name)

def login():
    tries=3
    for i in range(tries):
        username=input("Teacher Username: ")
        password=input("Password: ")
        print("Please Wait as we check your details. This could take a few seconds")
        for _ in range(6):
                print(".", end="", flush=True)
                time.sleep(0.5)
        print()
        with open("teacher.csv", "r") as file:
            csvreader=csv.reader(file)
            for row in csvreader:
                if row[0]==username and row[1]==password:
                    return "Successful Login"
                else:
                    tries-=1
            print("Failed Login attempt")
    return "Ran Out Of Tries"


def students():
    global name
    global student_id
    tries = 3
    while tries > 0:
        name = input("Please enter the student's name you want to know about: ")
        student_id = input("Please input their respective ID as well: ")
        student = Student(name, student_id)
        for _ in range(6):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print()
        if Student.search_student("student.csv", student.name, student.student_id):
            return "Found them!"
        else:
            tries -= 1
            print(f"Failed to find student. You have {tries} tries remaining.")
    return "Please try again later."


def data():
    final = Student.search_status("student.csv", name, student_id)
    n = name.upper()
    return f"{n} has {final} their homework"


def change():
    checking=Student.search_status("student.csv", name, student_id)
    print(f"As of right now {name} has {checking} their homwework")
    user=input("Would you like to change it? ").lower()
    if user=="no":
        sys.exit("See you soon")
    elif user=="yes":
        changing_i=input("What would you like to change it to? ").lower()
        Student.change_status("student.csv", name, student_id, changing_i)
        print("Please wait as we change it on the data base")
        for _ in range(6):
            print(".", end="", flush=True)
            time.sleep(0.25)
        print()
        return f"{name} has now {changing_i} their homework"

if __name__=="__main__":
    main()
