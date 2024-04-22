# input:5
# output:
# # 1
# # 1 2 1
# # 1 2 3 2 1
# # 1 2 3 4 3 2 1
# # 1 2 3 4 5 4 3 2 1

num=5#int(input("enter the number:"))

# output=[]
# values=[k for k in range(1,num)]
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print((str(values[:i-1][::-1])).strip("[]").replace(',',""),end="")
#     print()



for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")

    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()

