try:
    s = input("enter the S:")
    t = input("enter the T:")
    if len(s) == len(t):
        list_1 = []
        list_1.extend(t)
        # print(list_1)
        list_2 = []
        list_2.extend(s)
        # print(list_2)
        string = ""
        for i in list_1:
            for j in list_2:
                if i == j:
                    string += j
        if s == string:
            print(True)
        else:
            print(False)
    else:
        print(False)
except Exception as e:
    print(e)
finally:
    print("<------------------------>")
    print("Done")