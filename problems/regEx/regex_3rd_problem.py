#write a program that matches a string that has an O followed by two to three 'k'

import re

string=input("Enter The String:")
regex=re.findall("[k]",string)
len_regex=len(regex)
if len_regex==3 or len_regex==2:
    print("Matched")
else:
    print("Not matched")