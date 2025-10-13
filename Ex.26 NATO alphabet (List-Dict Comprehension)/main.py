# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

new_dict = {}

for (index, row) in data.iterrows():
    letter = row.letter
    code = row.code
    new_dict[letter] = code
# new_dict = {row.letter: row.code for (index, row) in data.iterrows()} #
print(new_dict)

word = input("Please input a word: ").upper()

output_list = [new_dict[letter] for letter in word]
print(output_list)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

