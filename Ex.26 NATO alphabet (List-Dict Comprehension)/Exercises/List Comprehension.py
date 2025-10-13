# # FOR LOOP:
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)


# # LIST COMPREHENSION (new_list = [NEW_ITEM for ITEM in LIST]) - used to iterate each element of the sequence to perform some operation to all:
# # LIST:
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

## STRING:
# name = "Oleksiy"
# new_list = [letter for letter in name]
# print(new_list)

# # RANGE:
# range_list = [i * 2 for i in range(1, 5)]
# print(range_list)

# # CONDITIONAL LIST COMPREHENSION (new_list = [NEW_ITEM for ITEM in LIST if TEST]):
# names = ["Alex", "Beth", "Arthur", "Oleksiy", "Ed"]
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)
# print(long_names)

# EXERCISES:
# 1)
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

# 2)
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

# 3)
# with open("file1.txt") as file1:
#     list1 = file1.readlines()
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
# result = [int(i) for i in list1 if i in list2]
# print(result)

# # DICTIONARY COMPREHENSION (new_dict = {NEW_KEY: NEW_VALUE for ITEM in LIST if TEST} // {NEW_KEY: NEW_VALUE for (KEY: VALUE) in DICT.ITEM()}):
# import random
# names = ["Alex", "Beth", "Arthur", "Oleksiy", "Ed"]
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

# EXERCISES:
#1)
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split()
# result = {word:len(word) for word in sentence}
# print(result)

# 2)
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

# # LOOPING THROUGH DICTIONARIES:
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# # LOOPING THROUGH A DATAFRAME:
import pandas

student_df = pandas.DataFrame(student_dict)
# print(student_df)

for (key, value) in student_df.items():
    print(key)
    print(value)

# # LOOP THROUGH ROWS OF A DATA FRAME:
for (index, row) in student_df.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
