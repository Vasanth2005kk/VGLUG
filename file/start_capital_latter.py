file_1=open('start_capital_latter_reading','r')
file_2=open('start_capital_latter_weriting','w')
for line in file_1:
    #print(line.capitalize(),end=" ")
    #print(line.title(),end=" ")
    file_2.write(line.title())
file_1.close()
file_2.close()