'''Revers words in string -reverse all the words in givan string without changing words position i string
sample input:
             Hello i am computer
sample output:
             olleh i ma retupmoc'''

str=input("Enter the string:").split(" ")
for i in str:
    print(i[::-1],end=" ")
