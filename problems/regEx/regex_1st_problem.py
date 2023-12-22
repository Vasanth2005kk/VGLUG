'''Write a program that matches a string that has an N followed by zero or more o's'''

import re

string=input("enter the string:")
string_1=string.lower()
regex=re.findall("^n*o$",string_1)
if regex:
    print(f"this ({string}) is matched")
else:
    print(f"this ({string}) is not matched")