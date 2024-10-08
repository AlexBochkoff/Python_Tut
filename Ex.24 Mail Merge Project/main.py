# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# PLACEHOLDER = "[name]"
with open('./Input/Names/invited_names.txt') as names:
    guests = names.readlines()

for n in range(len(guests)):
    guests[n] = guests[n].strip("\n")

with open("./Input/Letters/starting_letter.txt") as letter:
    template = letter.read()
    for name in guests:
        # stripped_name = name.strip()
        new_letter = template.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter for {name}.txt", mode="w") as new_file:
            new_file.write(new_letter)
