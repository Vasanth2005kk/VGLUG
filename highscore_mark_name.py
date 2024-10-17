'''write a python program to print the name of the student with highest mark. get the name & marks of N number of students as input.
(e.g):
enter the of students :3
enter names & markes of each student :vasanth
enter names & markes of each student :siva 54
enter names & markes of each student :parthi 86
output:
       parthi is highest mark.'''

# Prompt the user for the number of students
n = int(input("Enter the number of students:"))

# Initialize an empty list to store names and marks
list_1 = []

# Collect names and marks for each student
for i in range(n):
    name_mark = input("Enter names & marks of each student: ").split()
    list_1.append(name_mark)  # Add the list of name and mark to list_1

# Initialize an empty list to store marks
mark_list = []

# Extract marks from list_1 and convert them to integers
for j, k in list_1:
    mark_list.append(int(k))

# Find and print the student with the highest mark
for j, k in list_1:
    if int(k) == max(mark_list):  # Check if the current mark is the maximum
        print(f"{j} has the highest mark.")
