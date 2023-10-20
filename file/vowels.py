file_1=open('vowels_reading','r')
file_2=open('vowels_weriting','w')
vowels_list=["a","e","i","o","u","A","E","I","O","U"]
for lines in file_1:
    if lines[0] in vowels_list:
        file_2.write(lines)
        print(lines,end="")
file_1.close()
file_2.close()