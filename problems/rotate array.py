"""
k=3
1234567 --> 7654321
7654321 --> 567 4321
5674321 --> 567 1234 ==>5671234
"""

nums=[1,2,3,4,5,6,7]
k=3
nums_1=nums[::-1]
list_1=[]
for i in range(k):
    list_1.append(nums_1[i])
list_2=list_1[::-1]
list_3=[]
for j in nums_1:
    if j not in list_1 :
        list_3.append(j)
list_4=list_3[::-1]
for k in list_4:
    if list_2 not in list_4:
        list_2.append(k)
print(list_2)