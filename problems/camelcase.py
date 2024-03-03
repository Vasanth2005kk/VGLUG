try:
    user_string=input("Enter the string :").split()

    letters=[chr(i) for i in range(65,91)]
    count=0

    for word in user_string:
        if not (word[0] in letters or word[-1] in letters) :
            
            for word_chracter in word:
                
                if word_chracter.isupper():
                    count+=1
            if count == 1:
                print(word)
            count=0

except Exception as e:
    print("ERROR")