# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Mine
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
percentage = (int(tip)/100)+1
result = round((int(bill)/int(people))*percentage, 2)
print(f"Each person should pay: ${result}")

# Not mine:
# print("Welcom to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# bill_with_tip = tip/100*bill+bill
# bill_per_person = bill_with_tip/people
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")
