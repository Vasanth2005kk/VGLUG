file_1=open('words_count','r')
words=input("Enter the words and your choice:")
count=0
for line in file_1:
    count+=line.count(words)
    #print(line)
print(count)
file_1.close()