file_1=open('data_writing','w')
emt_list=[]
while True:
    line=input("enterthe string:")
    if line:
        emt_list.append(line)
    else:
        break
output=" ".join(emt_list)
print(output)
file_1.write(output)
file_1.close()