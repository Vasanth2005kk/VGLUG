#password chacking valide or unvalide 

string1=input("Enter the password :") #"Punith@123"

if len(string1)>=7:
    if not string1.isalnum():
        for i in string1:
            if i.isupper():
                print("valide")
                break
        else:
            print("invalide")
    else:
        print("invalide")    
else:
    print("you give the password is 7 letter above the letters!")