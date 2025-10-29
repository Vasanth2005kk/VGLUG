try:
    s = "A man, a plan, a canal:panama"
    string = ""
    for letters in s:
        if letters.isalpha():
            string += letters.lower()
    #print(string)
    reverse_string = string[::-1]
    #print(reverse_string)
    if string == reverse_string:
        print(True)
    else:
        print(False)
except Exception as e:
    print(e)
finally:
    print("<-------------------->\nDone")
