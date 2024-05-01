'''Revers words in string -reverse all the words in givan string without changing words pepole i string
sample input:
             Hello i am computer
sample output:
             olleh i ma retupmoc'''

string=input("Enter the string:").split(" ")
for i in string:
    print(i[::-1],end=" ")
print("helo")
