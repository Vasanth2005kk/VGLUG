'''
write the pattern for find the email id format
'''
try:
    import re

    email=input("Enter the mail : ")

    index_find=re.search("@",email).start()
    output=email[:index_find]

    if re.findall("@gmail.com$",email):
        if not re.findall("\W",output):
            print("successfully !")
        else:
            print("not this email !")
    else:
        print("not this email !")
except Exception as e:
    print("Error:",e)