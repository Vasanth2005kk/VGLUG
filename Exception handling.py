try:
    num = int(input("Enter the number:"))
    list_2 = []
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                if i * j * k == num:
                    print([i, j, k], "===>", end=" ")
                    list_1 = i + j + k
                    print(list_1)
                    list_2.append(list_1)
    # print(list_2)
    list_3 = []
    list_4 = []
    for i in list_2:
        if i not in list_3:
            list_3.append(i)
        elif i not in list_4:
            list_4.append(i)
    # print(list_3)
    # print(list_4)
    print("****************************************************")
    for i in list_4:
        if i:
            print("answer is: ===>", i)
except ValueError as error:
    print("ERROR ==>",error)
finally:
    print("",end=" ")
