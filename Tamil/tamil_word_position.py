# word position and replace the words in this program
# this normal 

tamil_wordes="""
பல நூற்றாண்டுகளாக செய்யுள் வடிவமே தமிழ் இலக்கியங்களிலும், தத்துவங்களிலும் பயன்படுத்தப்பட்டது. உரை வடிவம் இலக்கணங்களுக்கும், செய்யுள் விளக்கம் கூறவதற்கும், சாசனங்கள் (record) பதிவு செய்வதற்கும் பயன்படுத்தப்பட்டது. 20ஆம் நூற்றாண்டிலேயே உரை வடிவம் வளர்ச்சி செய்யுள் பெற்று, மக்களின் பல்வேறுபட்ட தேவைகளுக்கும் பயன்படுகின்றது. கட்டுரையே உரைநடை வெளிப்பாட்டின் முக்கிய வடிவம் ஆகும்.
""".strip().split()

input_word="செய்யுள்"
repace_word="வசந்த்"

index_position=0
position_numbers=[]

for i in tamil_wordes:
    index_position+=1
    if i == input_word:
        position_numbers.append(index_position)

for word_positions in position_numbers:
    tamil_wordes.pop(word_positions-1)
    tamil_wordes.insert(word_positions-1,repace_word)

print(" ".join(tamil_wordes))


# or

tamil_wordes="""
பல நூற்றாண்டுகளாக செய்யுள் வடிவமே தமிழ் இலக்கியங்களிலும், தத்துவங்களிலும் பயன்படுத்தப்பட்டது. உரை வடிவம் இலக்கணங்களுக்கும், செய்யுள் விளக்கம் கூறவதற்கும், சாசனங்கள் (record) பதிவு செய்வதற்கும் பயன்படுத்தப்பட்டது. 20ஆம் நூற்றாண்டிலேயே உரை வடிவம் வளர்ச்சி செய்யுள் பெற்று, மக்களின் பல்வேறுபட்ட தேவைகளுக்கும் பயன்படுகின்றது. கட்டுரையே உரைநடை வெளிப்பாட்டின் முக்கிய வடிவம் ஆகும்.
"""

input_word="செய்யுள்"
repace_word="வசந்த்"

replace_word_string=tamil_wordes.replace(input_word,repace_word)
print(replace_word_string)