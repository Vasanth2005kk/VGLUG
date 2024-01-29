#1
def letter(string):
    try:
        index=0
        output=[]

        for i in range(1,len(string)+1):
            output.append(i*string[index])
            index+=1
        print("-".join(output).title()) 
    except Exception as e:
        print("error:",e)
input_string=input("enter the string :")
letter(input_string)

#2
'''
def letters(string):
    try:
        index=0
        output=""
        for i in range(1,len(string)+1):
            print((i*string[index]).capitalize(),end="-")
            index+=1
        print()
    except Exception as e:
        print("Error",e)


input_string=input("Enter the string:")

letters(input_string)
'''