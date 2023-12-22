'''wrtie a program that matches a string that has an N followed by one or more o's.'''

import re

string=input("Enter The String:")
string_low=string.lower()
regex=re.findall("^n.+",string)
if regex:
    print(f"Matched: {string}")
else:
    print(f"Not Matched: {string}")