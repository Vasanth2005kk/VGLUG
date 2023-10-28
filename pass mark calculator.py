'''get input as string with comma seperated number denoting marks of list of student in class room.
print the array containg pass/fail respective to the input marks.
consider 35 and above are pass marks

sample input: 20,46,75,10
sample output: fail,pass,pass,fail
'''

studentmark=input("enter the mark:").split(" ")
list_1=studentmark
#print(list_1)
pass_or_fail=[]
for i in list_1:
    intger=int(i)
    if intger>=35:
        pass_or_fail.append("pass")
    else:
        pass_or_fail.append("fail")
#print(pass_or_fail)
for j in pass_or_fail:
    print(j,end=",")
