import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______) 
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]


choice = int(input("What do you choose? Type 0 for Rock, type 1 for Paper or type 2 for Scissors.\n"))

if choice >=3 or choice < 0:
    print("\nYou typed an invalid number. You lose.")
else:
    print(game_images[choice])

    machine_choice = random.randint(0,2)

    print("\nComputer chose:\n")    
    print(game_images[machine_choice])
    
    if choice == 0 and machine_choice == 2:
        print("\nYou win!")
    elif choice == 2 and machine_choice == 0:
        print("\nYou lose.")
    elif choice == machine_choice:
        print("\nIt's a draw.")   
    elif machine_choice > choice:
        print("\nYou lose.")
    elif choice > machine_choice:
        print("\nYou win!")