# 🚨 Don't change the code below 👇

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
#Write your code below this row 👇

total_hight = 0
number_of_students = 0

for hight in student_heights:
    total_hight = total_hight + hight
    # total_hight += hight
  
for student in student_heights:
    number_of_students += 1

avarage_height = total_hight / number_of_students

print(round(avarage_height))