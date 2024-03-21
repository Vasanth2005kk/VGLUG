try:
    string=input('enter the string:') 

    output=[]
    for i in range(len(string)):
        for j in range(i+2,len(string)+1):
            output.append(string[i:j])

    for k in output:
        if len(set(list(k)))==len(list(k)):
            print(k)
        else:
            print("NOT unic elements !")

except Exception as e:
    print("ERROR:",e)

