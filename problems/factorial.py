'''write a python program to find the sum of natural numbers upto N. 
sample input : 16
sample output : the sum of natural numbers upto 16 is 136'''

N=int(input("enter the value for N:"))
number=0
for i in range(1,N+1):
    number+=i
print(f"the sum of natural number upto {N} is {number}")