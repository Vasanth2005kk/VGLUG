"""Question:Write a Python program that takes an integer n as input and prints a diamond pattern of 2n-1 height.

Input
First line will contain an integer n representing the number of rows in the top half of the diamond.
Output
Print the diamond pattern of 2n-1 height.
Example:taking 5 as input

output:
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
"""

#code for this question.

n=int(input())
for i in range(1,n+1):
    for x in range(n-i):
        print("  ",end="")
    for t in range(1,i+1):
        print("*",end=" ")
    for k in range(t-1,0,-1):
        print("*",end=" ")
    print()
for w in range(n-1,0,-1):
    for v in range(n-w):
        print("  ",end="")
    for a in range(1,w+1):
        print("*",end=" ")
    for s in range(w-1,0,-1):
        print("*",end=" ")
    print()