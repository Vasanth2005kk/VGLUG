#write a program that matches a number at the end of a string.

import re
string=input("Enter the string and ending in digit:")
regex=re.findall("\d$",string)

if regex:
    print("Matched")
else:
    print("Not Matched")
