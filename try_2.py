import string as s

string = "welcome to vgluz"
word = ""
list_1 = []

for char in string:
    if char in s.ascii_lowercase:
        string_2= chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        word+=string_2
    else:
        word+=char

list_1.append(word)
print(word)
print(ord("w"))
print(ord("a"))