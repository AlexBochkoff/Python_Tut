# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Mine
a = int(weight)
b = float(height)
bmi = int(a/b**2)
print(bmi)

# Not mine:
# bmi = int(weight)/float(height)**2
# bmi_as_int = int(bmi)
# print(bmi_as_int)