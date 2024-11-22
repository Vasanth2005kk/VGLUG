"""Question:The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting with 0 and 1. The sequence follows the pattern:

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2) for n > 1

Your task is to write a function that calculates the Fibonacci sequence till nth term, for a given non-negative integer n. This is a function problem. You don't have to take any input. You must complete the function generate_fibonacci_series() that takes non-negative integer N as a paramter and returns the Fibonacci sequence for the given n.

Input
The first line will contain an integer N representing the number of terms
Output
The program should print the Fibonacci series up to N terms.
Example
Example 1:
Input:
5
Output:
0 1 1 2 3
Explanation:
0 1 1 2 3  is the fibonacci series up to 5th term.

Example 2:
Input:
6
Output:
0 1 1 2 3 5
Explanation:
0 1 1 2 3 5 is the fibonacci series up to 5th term."""

#code for this question.

def generate_fibonacci_series(N):
    last_term=1
    sec_last=0
    for i in range (1,N+1):
        if i==1:
            print(0,end=" ")
        elif i==2:
            print(1,end=" ")
        else:
            current_term=last_term+sec_last
            print(current_term,end=" ")
            sec_last=last_term
            last_term=current_term