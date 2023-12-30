'''write a python program to remove special caracters from an input string. the special characters to be removed are !@#$%

sample input: wellcome ! t@o v$glu%g
sample output: wellcome to vglug'''

string="wellcome ! t@o v$glu%g"
special_crate=["!","@","#","$","%"]
letter=[]
output=""
for i in string:
    if i in special_crate:
        continue
    else:
        output+=i
print(output)    

# or

'''from string import punctuation

string="wellcome ! t@o v$glu%g"
output=""
for i in string:
    if i in punctuation:
        continue
    else:
        output+=i
print(output)
'''
'''
string="wellcome ! t@o v$glu%g"
spcila_cracter="!@#$%^&*()+_?><"
new_string=string
print(new_string)
for i in spcila_cracter:
    new_string=new_string.replace(i,"")
print(new_string)
'''