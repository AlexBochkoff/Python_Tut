# 🚨 Don't change the code below 👇

student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
#Write your code below this row 👇

total_height = 0
number_of_students = 0

for height in student_heights:
    total_height = total_height + height

    # total_height += height
  
for student in student_heights:
    number_of_students += 1

average_height = total_height / number_of_students

print(round(average_height))