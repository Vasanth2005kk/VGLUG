#nested loops
n=int(input("Give the n value :"))
#2 for loops are used inside of a for loops
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="   ") 
    print("\n")
