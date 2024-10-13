number=int(input())
for i in range(1,number+1):
    print(i*"*")

# or 

print("<--------------------------->")    

for i in range(1,number+1):
    for j in range(i):
        print("*",end="")
    print()