import string as s
word="good morning guys ! 1234"
string=0
number=0
special_character=0
for i in word:
    if i.isalpha():
        string+=1
    elif i.isdigit():
        number+=1
    elif i in s.punctuation:
        special_character+=1
print("Word full length:",len(word))
print("letters:",string)
print("Numbers:",number)
print("Special_characters:",special_character)

'''string="good morning ! 1234"
list_1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number_list=['1','2','3','4','5','6','7','8','9','0']
letter=0
number=0
sp_c=0
space=" "
for i in string:
    if i in list_1:
        letter+=1
    elif i in number_list:
        number+=1
    else:
        if i not in space:
            sp_c+=1
print(letter)
print(number)
print(sp_c)'''
