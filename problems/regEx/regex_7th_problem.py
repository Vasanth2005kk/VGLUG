'''
write the pattern for find the email id format
'''

import re

email="vasanth#2005kk@gmail.com"


index_find=re.search("@",email).start()

output=email[:index_find]

if re.findall("",output):
    print("yes")

#if re.findall("@gmail.com$",email):
#    print("its right")
    
    