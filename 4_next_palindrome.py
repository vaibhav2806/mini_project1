'''
The task you have to perform is “The Next Palindrome.” 
This task consists of a total of 15 points to evaluate your performance.

Problem Statement:-
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. 
You have to find the next palindrome corresponding to that number. 
Your first input should be the number of test cases and then take all the cases as input from the user.

Input:
3

451

10

2133

Output:
Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222
'''
def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]
    
if __name__ == "__main__":

    test_case = int(input("Enter the number of cases you want to test: "))
    numbers = []

    for i in range(test_case):
        number = int(input("Enter the number: "))
        numbers.append(number)

    for i in range(test_case):
        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")