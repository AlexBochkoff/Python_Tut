# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Mine:
names_amnt = len(names)

import random
random_name = random.randint(0, (names_amnt-1))

who_will_pay = names[random_name]

print(f"{who_will_pay} is going to buy the meal today!")

# Not mine:
who_will_pay = random.choice(names)
print(f"{who_will_pay} is going to buy the meal today!")
