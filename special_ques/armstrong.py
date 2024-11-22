"""Question:You are given a number. Your task is to check if this number is an Armstrong number.

An Armstrong number  is a number that is equal to the sum of its own digits, each raised to the power of the number of digits.

User Task:
This is a function problem. You don't have to take any input. You are required to complete the function isArmstrong() that takes an integer N as a parameter and returns True if the number is an Armstrong number, otherwise returns False.

Input:First line will contain an Integer N.

Output:Return True if the number is Armstrong, otherwise return False.
Example:
Input:
153
Output:
True

Input:
123
Output:
False"""

# code for the ques:
def isArmstrong(N):
    digits=list(map(int,str(N)))
    num_digits = len(digits)
    armstrong_sum = sum(digit**num_digits for digit in digits)
    
    
    if armstrong_sum==N:
        return("True")
    else:
        return("False")