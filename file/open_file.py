file_1=open("open_file_reading","r")
file_2=open("open_file_weriting","w")
for line in file_1:
    #print(line,end="")
    file_2.write(line)
file_1.close()
file_2.close()