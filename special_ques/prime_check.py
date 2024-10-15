"""Question: In the Kingdom of Primalia, numbers hold special powers, and prime numbers are considered the most powerful. Help the royal mathematician by writing a program that checks if a given number is prime or not.

Prime number is defined as the number which has exactly two factors : 1 and the number itself.

Task:
This is a function problem. You don't have to take any input. You are required to complete the function is_prime() which takes an integer n as a parameter and returns True if the number is prime, otherwise returns False.
Input
First line will contain an integer n.

Constraints:
0 <= n <= 10^8
Output
Return True if the number is prime, otherwise return False
Example
Input:
17

Output:
True

Explanation:
The number 17 is a prime number because it has no divisors other than 1 and itself."""

#code for this question.
def is_prime(n):
    if n==2:
        return "True"
    for i in range (2,n):
        if  n>2 and n%i==0:
            return "False"
        elif n%i!=0:
            return "True"