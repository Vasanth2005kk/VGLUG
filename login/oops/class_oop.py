class Usre:
    def __init__(self,key):
        if key:
            self.user_name=input("Enter your name :")
            self.password=input("Enter the password :")
            self.retrypassword=input("Retry password :")
        else:
            self.user_name_login=input("User name :")
            self.password_login=input("password :")

    def use_name_check(check_name):
        data=[]
        with open("text.txt","r") as f:
            for i in f.readlines():
                output=i.strip("[]\n")
                data.append(output.split(","))
            for j in data:
                if j[0] == check_name:
                    return True
                else:
                    return False    

    def regestr(self):

        if self.user_name:
            
            if Usre.use_name_check(self.user_name):
                print("alredy user name difined !")
            
            else:
                if self.password==self.retrypassword:
                    with open("text.txt","a") as file_appending:
                        file_appending.write(f"[{self.user_name},{self.password}]\n")
                
                else:
                    print("password is not mached!")
        else:
            print("type for u name") 


    def login(self):
        data=[]
        with open("text.txt","r") as f:
            for i in f.readlines():
                output=i.strip("[]\n")
                data.append(output.split(","))
            for i in data:
                if self.user_name_login==i[0]:
                    if self.password_login==i[1]:
                        print("scessfully !")
                        break
            else:
                print("{msg:^50}".format(msg="------------------ not this name ----------------".title()))
