try:
    list_1=input().split(" ")

    def ascci_counts(list_1):
        ascci_letters={
            "a":1,
            "b":2,
            "c":3,
            "d":4,
            "e":5,
            "f":6,
            "g":7,
            "h":8,
            "i":9,
            "j":10,
            "k":11,
            "l":12,
            "m":13,
            "n":14,
            "o":15,
            "p":16,
            "q":17,
            "r":18,
            "s":19,
            "t":20,
            "u":21,
            "v":22,
            "w":23,
            "x":24,
            "y":25,
            "z":26,
            }

        storde=[]
        count=0
        for i in list_1:
            for j in set(i):
                count+=ascci_letters.get(j)
            storde.append(count)
            count=0
        return storde
    

    def counts(list_1):
        letter_lenth_count=[]

        for i in list_1:
            letter_lenth_count.append(len(i))
        return letter_lenth_count


    num=(len(counts(list_1)))
    index=0
    output=[]

    if num==5:
        for i in range(num):
            if (counts(list_1)[index])>(ascci_counts(list_1)[index]):
                output.append(True)
            index+=1
        if output.count(True)>=5:
            print("Your Lucky I Will Gift for Ice Cream")
        else:
            print("Better Luck Next Time")
    else:
        print("Better Luck Next Time")

except Exception as e:
    print("Error :",e)