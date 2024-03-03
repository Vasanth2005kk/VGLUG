
try :
    string_and_num=input().split(" ")


    if len(string_and_num[0]) > int(string_and_num[1]):

        output=string_and_num[0][int(string_and_num[1])-1:]
        
        print(output+string_and_num[0][0:int(string_and_num[1])-1])
    else:
        print("outof range in seconde  value !")

except Exception as e:
    print("ERROR")
