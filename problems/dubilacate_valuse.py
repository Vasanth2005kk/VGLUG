s=['a', 'a', 'a', 'b', 'd', 'd', 'd']

list_1=[]
list_2=[]

for i in s:
    if not i in list_1:
        list_1.append(i)
    else:
        list_2.append(i)

print('real valuse',list_1)
print('dubilicate valuse',list_2)