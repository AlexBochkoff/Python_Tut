# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Mine:
# left = 90 - int(age)
# days = 365*left
# weeks = 52*left
# months = 12*left

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Not mine:
age_as_int = int(age)
left = 90 - age_as_int
days = left*365
weeks = left*52
months = left*12
message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)