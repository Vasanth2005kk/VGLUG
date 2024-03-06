try:
    def letters(l):
        s=0
        print(l[0])
        if len(l) > s:
            s+=1
            letters(l[s:])


    letter="vasanth"
    letters(letter)

except Exception as e:
    pass