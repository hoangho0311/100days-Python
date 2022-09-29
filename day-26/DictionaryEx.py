# sentence = "what is the airspeed velocity of an unladen swallow?";
#
# result = {item:len(item) for item in sentence.split()}
# print(result)

# weather = {
#     "monday":12,
#     "tuesday":14,
#     "wednesday":15,
#     "thurday":14,
#     "friday":21,
#     "saturday":22,
#     "sunday":24
# }
#
# tem_f = {weather:tem*9/5+32 for (weather,tem) in weather.items()}
# print(tem_f)

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
list_data = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("enter a word").upper()
list_word = [ list_data[letter] for letter in word ]
print(list_word)