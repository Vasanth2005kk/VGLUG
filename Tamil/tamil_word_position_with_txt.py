# position checking

def position_checking(input_word):

    f=open('tamil.txt','r+')

    text_file=f.readlines()
    text_file_length=len(text_file)

    json_formate={}
    textline_and_position_values=[]
    position_number=0

    for index in range(text_file_length):
        positions=[]
        positions.append(f" line {index+1} positions ")
        
        for words in text_file[index].split():
            position_number +=1
            if words == input_word:
                positions.append(position_number)
        position_number=0

        if len(positions) != 1:
            json_formate.update({positions[0]:positions[1::]})

    return json_formate

# answer=position_checking(input_word='செய்யுள்')
# print(answer)


# text file replace the values 

def file_replce_word(file_name,word,replace_word):
    reading_file_output=[]

    with open(file_name,"r") as reading_file:
        reading_file_output.append(reading_file.read().strip())


    with open(file_name,"w") as write_file:

        for i in reading_file_output:
            replace_word_string=i.replace(word,replace_word)
            write_file.write(replace_word_string)


file_name="tamil.txt"
word="ஆகும்"
replace_word="end"

file_replce_word(
    file_name=file_name,
    word=word,
    replace_word=replace_word)