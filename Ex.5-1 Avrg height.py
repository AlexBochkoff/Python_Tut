# 🚨 Don't change the code below 👇

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
#Write your code below this row 👇

total_height = 0
number_of_students = 0

<<<<<<< HEAD
for height in student_heights:
    total_height = total_height + height
=======
for hight in student_heights:
    total_hight = total_hight + hight
>>>>>>> f78e0937583423b5aa5f0d5e03524b680de5d9f5
    # total_hight += hight
  
for student in student_heights:
    number_of_students += 1

avarage_height = total_height / number_of_students

print(round(avarage_height))