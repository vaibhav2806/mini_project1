'''
The task you have to perform is “Your Age In 2090”. 
This task consists of a total of 10 points to evaluate your performance.

Problem Statement:-
Take age or year of birth as an input from the user. Store the input in one variable. 
Your program should detect whether the entered input is age or year of birth and tell the user when they will 
turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

--> Do not use any type of modules like DateTime or date utils. (-5 points)
--> Users can optionally provide a year, and your program must tell their age in that particular year.(3points)

-->Your code should handle all sort of errors like:(2 points)
->You are not yet born
->You seem to be the oldest person alive
->You can also handle any other errors, if possible!
'''
def age(inp):
    
    if inp < 100:
        temp = 100 - inp
        print(f"You will turn 100 in {temp+2020} years.")

    elif inp >=100 and inp <=120:
        print("You are the oldest person alive.")

    elif inp < 0:
        print("You are not yet born.")

    elif inp == 0:
        print(f"Welcome to this world newbi. You will turn 100 in 100 years.")

    else: 
        print("Please enter correct details for acurate result.")


def dob(inp):

    if inp < 2020 and inp > 1850:
        temp = 2020 - inp
        print(f"You are {temp} years old")
        hund = 100 - temp
        print(f"You will turn 100 in {hund+2020} years.")

    elif inp > 2020:
        print("You are not yet born.")

    elif inp == 2020:
        print("Welcome to this world newbi. You are 0 years old.")

    else:
        print("Please enter correct details for acurate result.")


def random_year(inp,age):

    if inp > 2020:
        temp = inp - 2020
        age = age+temp
        print(f"In {inp} year you will be {age} years old.")

    elif inp <= 2020:
        temp = 2020 - inp 
        age = age - temp
        if age == 0:
            print(f"You were born in this year {inp}")
        elif age < 0:
            print("The year you entered was before your birth.")
        else:
            print(f"In year {inp} you were {age} year old.")

    else:
        print("Please enter correct detials for acurate results. ")


if __name__ == "__main__":

    inp = int(input("Enter age or year of birth: "))
    if inp < 1000:
        age(inp)
    elif inp >1000:
        dob(inp)
    else:
        print("Enter correct details.")
    
    imp2 = int(input("Do you want to know your age in any particular year? Press 1 for yes and 2 for no:  "))
    if imp2 == 1:
        age = int(input("Enter your age:"))
        inp = int(input("Enter the year in which you want to know your age: "))
        random_year(inp,age)
    else:
        print("Thank You")
        exit()
