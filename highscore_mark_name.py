'''write a python program to print the name of the student with highest mark. get the name & marks of N number of students as input.
(e.g):
enter the of students :3
enter names & markes of each student :vasanth
enter names & markes of each student :siva 54
enter names & markes of each student :parthi 86
output:
       parthi is highest mark.'''

n=int(input("enter the student:"))
list_1=[]
for i in range(n):
    name_mark=input("enter names & markes of each student :").split()
    list_1.append(name_mark)
mark_list=[]
for j,k in list_1:
    mark_list.append(int(k))

for j,k in list_1:
    if int(k)==max(mark_list):
        print(f"{j} is highest mark.")