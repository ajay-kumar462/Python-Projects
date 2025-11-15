student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

# nato_dict = nato_dataframe.to_dict()
# print(nato_dict)

nato_dict = {row.letter:row.code for (index, row) in nato_dataframe.iterrows()}
# print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ")
letter_list = [letter for letter in word]

# List
helping_words = [nato_dict[letter.upper()] for letter in letter_list]
print(helping_words)

#Dictionary - my own version -> Gives dictionary using the word "hello" but "l" appears only once because dictionary does not take same key twice.

# helping_words = {letter:nato_dict[letter.upper()] for letter in letter_list}
# print(helping_words)