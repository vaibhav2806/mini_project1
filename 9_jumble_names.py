'''
Problem Statement:-
Its result day at school and not everyone is happy. 
You decided to make your friends laugh by jumbling their names to come up with some funny names.

Your program should take the number of names and the names separated by space as input. 
Output should be funny names in the same order.

Input:
Enter number of friends:

3

Enter the name of your 3 friends:

Rohan Das

Shubham Agarwal

Ritesh Arora

Output:
Ritesh Das

Shubham Arora

Rohan Agarwal
'''

import random 

friends = int(input("Enter the number of friends you have: "))
names = []
firstName = []
lastName = []
for i in range(friends):
    name = input(f"Name {i+1}: ")
    names.append(name)

for item in names:
    a,b = item.strip().split(" ")   #or splitNames = item.strip().split(" ") 
    firstName.append(a)             #or firstName.append(splitNames[0])
    lastName.append(b)              #or lastName.append(splitNames[1])

randomList = []
while True:
    if len(firstName)!=0 and len(lastName)!=0:
        ra = random.choice(firstName)
        rb = random.choice(lastName)
        jumblename = ra+" "+rb
        randomList.append(jumblename)
        firstName.remove(ra)
        lastName.remove(rb)
    else:
        break

for item in randomList:
    print(f"Funny name {item}: ")







