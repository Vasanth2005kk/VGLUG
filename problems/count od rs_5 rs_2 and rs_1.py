input_number=int(input("Enter the number:"))

five=input_number//5
five_remainder=input_number-(five*5)

two=five_remainder//2
two_remainder=input_number-(two*2)-(five*5)

one=two_remainder

if five != 0:
    print("Count of Rs 5 :",five)
    if two !=0 :
        print("Count of Rs 2 :",two)
        if one != 0:
            print("Count of Rs 1 :",one)