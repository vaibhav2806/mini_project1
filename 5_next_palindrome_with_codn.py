'''
The task you have to perform is “Palindromify the List.” 
This task consists of a total of 10 points to evaluate your performance.

The task is very similar to the previous one i.e. Tutorial #109 ( Pyhton Problem 4)

Problem Statement:-
You are given a list that contains some numbers. You have to print a list of next palindromes only if the 
number is greater than 10; otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
'''

def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n 

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":

    n = int(input("Enter number of test case: "))
    numbers = []
    list = []
    for i in range(n):
        number = int(input("Enter a number: "))
        numbers.append(number)

    for i in range(n):
        if numbers[i] > 10:
            list.append(next_palindrome(numbers[i]))
        else:
            list.append(numbers[i])
    print(list)