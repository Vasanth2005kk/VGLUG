call_name_or_number=input("Enter the name or mobile number :")
call={
    "8220921078":"vasanth",
    "9345858351":"santhosh",
    "9344838281":"ranjith",
    "1236537646":"vasanth"
}
for number,name in call.items():
    if call_name_or_number==name:
        print(f"'{name}' number is : {number}")
    elif call_name_or_number==number:
        print(f"the number:{number} is ==> {name}")
    elif call_name_or_number  not in name or call_name_or_number not in number:
            print("not this moblie number !")
            break