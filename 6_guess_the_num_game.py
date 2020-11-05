'''
Problem Statement:-
Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. 
a and b are inputs taken from the user. Your friend is player 1 and plays first.
He will have to keep choosing the number and your program must tell whether the number is greater than 
the actual number or less than the actual number.
Log the number of trials it took your friend to arrive at the number. 
You play the same game and then the person with minimum number of trials wins! 
Randomly generate a number after taking a and b as input and don’t show that to the user.

Input:
Enter the value of a

4

Enter the value of b

13

Output:
Player1 :

Please guess the number between 4 and 13

5

Wrong guess a greater number again

8

Wrong guess a smaller number again

6

Correct you took 3 trials to guess the number

Player 2:

Correct you took 7 trials to guess the number

Player 1 wins!
'''
import random

def guess_game(a,b,c1):
    count = 0
    flag = 0
    while flag != 1:
        guess = int(input(f"Please guess the number between {a} and {b} : "))
        if guess>c1:
            print("Wrong guess you entered a greater number ")
            count += 1

        elif guess<c1:
            print("Wrong guess you entered a smaller number ")
            count += 1

        else:
            print(f"Correct you took {count+1} trials to guess the number")
            flag = 1
            return count
            
if __name__ == "__main__":
        
    a = int(input("Enter the minimum range: "))
    b = int(input("Enter the maximum range: "))
    c1 = random.randint(a,b)

    print("Player 1 : ")
    g1 = guess_game(a,b,c1)

    print("\nPlayer 2 : ")
    g2 = guess_game(a,b,c1)


    if g1 > g2:
        print("Player 2 wins")
    elif g2 > g1:
        print("Player 1 wins")
    else:
        print("Draw ")


    

        




