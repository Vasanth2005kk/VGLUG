'''
write a python program that matches a word containing 'z', not the start or end of the word.
'''

import re

string=input().lower()

if re.findall("^z",string):
    print(" Not starting the in 'Z' ")
elif re.findall("z$",string):
    print("Not end in the 'z' ")
else:
    print("Successfully")