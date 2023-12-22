#Write a program that matches a word at the beginning of a string

import re

string=input("Enter The String:")
regex=re.findall("^\w",string)

if regex:
    print(f"Matched: {string}")
else:
    print(f"Not Matched: {string}")