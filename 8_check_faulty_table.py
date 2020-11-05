'''
Problem Statement:-
Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a,
given number and put one of the values (randomly generated) as wrong.

Rohan Das did this to fool his classmates and make them commit a mistake in a test. 
You cannot tolerate this!
 
So you decided to use your python skills to counter Rohan’s actions by writing a python program that 
validates Rohan’s multiplication table.

Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.

Note: Rohan’s function returns a list of numbers like this

Rohan Das’s Function Input:
rohanMultiplication(6)

Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]

You have to write a function isCorrect(table, number) and return the index where rohan’s function 
is wrong and print it to the screen! If the table is correct, your function returns None
'''
# NOTE: Enumerate method comes with an automatic counter/index to each of the items present in the list. 
# The firstindex value will start from 0. 
# You can also specify the startindex by using the optional parameter startIndex in enumerate.

import random

def rohanTable(n):
    index = random.randint(0,9)
    rohanList = [n*i for i in range(1,11)]
    rohanList[index] = rohanList[index] + random.randint(1,5)
    return rohanList

def isCorrect(n,rohanList):
    for i in range(1,11):
        if rohanList[i-1] != i*n:
            return i-1
        
    return None

if __name__ == "__main__":
    n = int(input("Enter the number of which table you require: \n"))
    rohanList = rohanTable(n)
    print(rohanList)
    wrongIndex = isCorrect(n,rohanList)
    print (f"The table is wrong at index {wrongIndex}")
    
