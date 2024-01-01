file_heandling=open("data_file.txt","a")
file_heandling_read=open("data_file.txt","r")

print("1 press login page")
print("2 press regester page")

key=int(input("Enter :"))

data_file_store=[]
for i in file_heandling_read:
        data_file_store.append(i.split(","))
# login table
if key==1:
    user_name=input("User Name:")
    password=input("Password:")
    for j in data_file_store:
        if user_name==j[0]:
            if password+"\n"==j[1]:
                print("\n    Succefull ")
            else:
                print("\n    Password is Not mached\n")
        else:
            print("\n    Username is Not mached\n")

#crate table
if key==2:
    create_user_name=input("Enter your name :")
    create_password=input("Create your password  :")
    return_password=input("Return your passsword :")
    if create_password==return_password:
        file_heandling.write(f"{create_user_name},{create_password}\n")
        print("\n       Succefull\n")
    else:
        print(f"\nCreate your password and Retrun your password not mach !\n")
        print(f"proof:\n       {create_password}\n       {return_password}\n")
