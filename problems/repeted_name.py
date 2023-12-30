num=int(input("enter the number:"))
name_stord=[]
for _ in range(num):
    n=input("enter the name:")
    name_stord.append(n)
for i in set(name_stord):
    print("name:",i)    