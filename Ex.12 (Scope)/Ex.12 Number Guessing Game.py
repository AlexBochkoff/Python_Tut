import random as r
from NumberGuessingArt import logo

# print(logo)
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100")

# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# if difficulty == 'easy':
#     number_of_attempts = 10
# elif difficulty == 'hard':
#     number_of_attempts = 5
# print(f"You have {number_of_attempts} attempts remaining to guess the number.")

# the_number = r.randint(1, 100)
# #print(f"Pssst, the correct answer is {the_number}.")
# is_over = False

# while not is_over:
#     guess_number = int(input("Choose your number: "))
        
#     if guess_number <= 0 or guess_number > 100:
#         print("The number is out of range. Please try again.")
#         is_over = True
#         break
#     elif guess_number == the_number:
#         print(f"You got it! The answer was {the_number}.")
#         is_over = True
#         break
#     elif guess_number < the_number:
#         print("Too low.")
#         number_of_attempts -= 1
#     elif guess_number > the_number:
#         print("Too high.")
#         number_of_attempts -= 1
        
#     if number_of_attempts == 0:
#         is_over = True
#         print("You lose.")
#         break

#     print("Guess again.")
#     print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    
    
#Not mine:
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = r.randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
