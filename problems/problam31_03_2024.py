try:

    def string_split(string):
        string=string.upper()
        value=''
        split_value=[]

        for i in string:
            if i in ['1','2','3','4','5','6','7','8','9','0']:
                if 'S' == string[(string.find(i))-1]:
                    value+=string[(string.find(i))-1]+i
                    split_value.append(value)
                    value=''
            elif i =='s' or i == 'S':
                continue
            else:
                split_value.append(i)
        return split_value

    number=[1,2,3,4,5,6]
    methods=string_split('rltdrrtrs22s1')
    print(methods)

    r_count=0
    for i in methods:
        if i=='R':
            r_count+=1
        elif i == 'L':
            r_count-=1
        elif i == 'T':
            number[r_count]=number[r_count]+1
        elif i == 'D':
            number[r_count]=number[r_count]-1
        elif i.startswith('S'):
            s_split=list(i)
            if len(number)>= int(s_split[1]):
                copy_number = number.copy()
                number[r_count] = number[int(s_split[1]) - 1]
                number[int(s_split[1]) - 1] = copy_number[r_count]

    print(number)

except Exception as e:
    print(e)