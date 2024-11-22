"""Question: Given a number n, determine whether it qualifies as a Strong Number or not.

A Strong Number is defined as a number where the sum of the factorials of its digits equals the original number itself.
Factorials is the product of all positive integers up to a given number x.
You need to return 1 if the given number is Strong number, otherwise 0.

Note:- This is a functional problem. You do not need to take any input. You just need to complete the function and just return 1 or 0 accordingly.
Input
First line contains an Integer n.
Output
Print 1 if n is a Strong Number, otherwise print 0.
Example
Input
145
Output
1
Explanation
1! + 4! + 5! = 145 So, 145 is a Strong
Number and therefore the Output 1.

Input
14
Output
0
Explanation
1! + 4! = 25 So, 14 is not a Strong
Number.
"""
# code for this question
def is_strong_number(n):
    count=0
    temp=n
    fact=1
    while temp!=0:
        fact=1
        last_digit=temp%10
        temp=temp//10
        for i in range (1,last_digit+1):
            fact=fact*i 
        count=count+fact
    if count==n:
        return 1
    else:
        return 0