try:
    def _task(string1,string2):
        list_1=[]

        for i in string2:
            list_1.append(i)
        
        for j in string1:
            if j in list_1:
                list_1.remove(j)
     
        output=""
        for i in list_1:
            output+=i
        return output

    string1=input().split(" ")

    output=_task(string1[0],string1[1])
    if output:
        print("Answer:",output)
    else:
        print("Not Answer !")

except Exception as e:
    print(e)