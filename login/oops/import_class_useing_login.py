import class_oop as e

class_varible=e.Usre

print("1.register \n2.login \n{:^50}".format("-----closed for commed ( 0 or exit )-----"))

keys=input(" Enter :")

if keys=="1":
    output=class_varible(key=True)
    output.regestr()
elif keys == "2":
    output=class_varible(key=False)
    output.login()
elif keys.lower() == "exit" or keys=="0":
    pass
else:
    print("Not this key ")