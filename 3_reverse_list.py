'''
The task you have to perform is “Foods and Calories.” 
This task consists of a total of 15 points to evaluate your performance.

Problem Statement:-
You visited a restaurant , and the food items in that restaurant are sorted, 
based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reverse a list:

Inbuild method of python
List name [::-1] slicing trick
Swapping the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]

->Input:
Take a list as an input from the user
[5, 4, 1]

->Output:
[1, 4, 5]

[1, 4, 5]

[1, 4, 5]
'''
n = int(input("Enter the number of items you want to enter: "))
list = []
for i in range (n):
    itemcalo = int(input("Enter the element: "))
    list.append(itemcalo)

# Method 1
# list = list[::-1]
print(list[::-1])

# Method 2
list.reverse()
print(list)

# Method 3
for i in range(len(list)//2):
    list[i] , list[len(list)-i-1] = list[len(list)-i-1] , list[i]
    print(list)