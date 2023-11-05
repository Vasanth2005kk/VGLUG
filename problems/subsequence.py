try:
    s = input("Enter the S:")
    t = input("Enter the T:")
    list_1 = []
    list_1.extend(s)
    list_2 = []
    list_2.extend(t)
    string = ""
    for i in list_2:
        for j in list_1:
            if i == j:
                string += j
    if s == string:
        print(True)
    else:
        print(False)
except Exception as e:
    print("ERROR:",e)
finally:
    print("Done")