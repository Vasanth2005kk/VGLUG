num=int(input("enter the number:"))

stored_list=[]
for _ in range(num):
    name_age_gender=input("enter th name , age and gender:").split(" ")
    stored_list.append(name_age_gender)

for name,age,gendr in stored_list:
    if "male"==gendr or "m"==gendr:
        print(f"Mr.{name}")
    elif "female"==gendr or "f"==gendr:
        print(f"Ms.{name}")
        
        