"""Question:In Newton School of Technology, student Govind is fascinated by perfect number. He wants to check if a given number is perfect number or not. Help Govind by writing a program that checks if a given number is perfect or not.
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
A divisor of an integer x is an integer that can divide x completely.

This is a functional problem. You do not need to take any input. You just need to complete the function, and return the output.

Input
First line contains an integer n
Output
Print True if the number is perfect number, otherwise print False.
Example
Input
28
Output
True
Explanation
28 = 1 + 2 + 4 + 7 + 14.

Input
5
Output
False
"""

#code for this question.
def checkPerfectNumber(num):
    count=0
    for i in range(1,n):
        if n%i==0:
            count=count+i
        else:
            count=count+0
    if count==n:
        return(True)
    else:
        return(False)