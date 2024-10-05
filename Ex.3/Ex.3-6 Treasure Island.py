print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction1 = input("You\'re on the crossroad. Where do you wanna go next? Left or right?\n").lower()

# Mine (Not mine: to use .lower (which is lower case) on input to decrease coding and to use string in if-part; also delete unnecessary elif for game over)

# left = "Left".lower()
# right = "Right".lower()

if direction1 == "left":
    print("You have reached a lake.")
    action1 = input("What are you gonna do next? Wait or swim?\n").lower()

    # wait = "Wait".lower()
    # swim = "Swim".lower()

    if action1 == "wait":
        print("A boat has arrived. And now you can safly cross over the lake.")
        print("After some time you have reached a house with three doors: red, yellow, and blue.")
        choice1 = input("Which door would you choose?\n").lower()

        # red = "Red".lower()
        # yellow = "Yellow".lower()
        # blue = "Blue".lower()

        if choice1 == "yellow":
            print("You win! The treasure is yours!")
        elif choice1 == "red":
            print("Shit! The room is on fire and you are on fire as well!\nGame over!")
        elif choice1 == "blue":
            print("Well, you were eaten by wild beasts...\nGame over!")
        else:
            print("Game over!")

    # elif action1 == "swim":
    #     print("You were attacked by a trout.\nGame over!")
    else:
        print("You were attacked by a trout.\nGame over!")

# elif direction1 == "right":
#     print("You fell into a hole.\nGame over!")
else:
    print("You fell into a hole.\nGame over!")