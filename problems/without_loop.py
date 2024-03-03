# print for 1 to 100 in without loop

def fun(x):
    if x<=100:
        print(x,end=" ")
        x+=1
        fun(x)


x=1
fun(x=x)