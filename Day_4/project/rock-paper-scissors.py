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

#Write your code below this line 👇

user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))




output = [rock, paper, scissors]
output_words = ["Rock", "Paper", "Scissors"]
options = [0, 1, 2]

computer_choise = random.choice(options)


if user_choise >= 3 or user_choise < 0:
  print("you typed an ivalid number, You lose")
elif computer_choise == 0 and user_choise == 2:
  print(f"user choise:{output[user_choise]}\ncomputer choise: {output[computer_choise]}")
  print("computer is the Winer")
elif computer_choise == 2 and user_choise == 0:
  print(f"user choise:{output[user_choise]}\ncomputer choise: {output[computer_choise]}")
  print("User is the Winer")

elif computer_choise == 2 and user_choise == 1:
  print(f"user choise:{output[user_choise]}\ncomputer choise: {output[computer_choise]}")
  print("computer is the Winer")
elif computer_choise == 1 and user_choise == 2:
  print(f"user choise:{output[user_choise]}\ncomputer choise: {output[computer_choise]}")
  print("User is the Winer")

elif computer_choise == 1 and user_choise == 0:
  print(f"user choise:{output[user_choise]}\ncomputer choise: {output[computer_choise]}")
  print("computer is the Winer")
elif computer_choise == 0 and user_choise == 1:
  print(f"user choise:{output[user_choise]}\ncomputer choise: {output[computer_choise]}")
  print("User is the Winer")
else:
  print(f"user choise:{output[user_choise]}\ncomputer choise: {output[computer_choise]}")
  print("not winer")

if user_choise <= 3 and user_choise >= 0:
  print(f"user: {output_words[user_choise]}\ncomputer: {output_words[computer_choise]}")