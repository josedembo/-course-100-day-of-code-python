# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# cont_t = both_names.count("t")
# cont_r = both_names.count("r")
# cont_u = both_names.count("u")
# cont_e = both_names.count("e")

# cont_l = both_names.count("l")
# cont_o = both_names.count("o")
# cont_v = both_names.count("v")
# cont_e = both_names.count("e")
words = "truelove"
name1 = name1.lower()
name2 = name2.lower()
both_names = name1+name2

first_digit = 0
second_digit = 0

first_digit += both_names.count("t") + both_names.count("r") + both_names.count("u") + both_names.count("e")
second_digit += both_names.count("l") + both_names.count("o") + both_names.count("v") +  both_names.count("e")

score = str(first_digit) + str(second_digit)
score_int = int(score)

if score_int < 10 or score_int > 90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int > 40 and score_int < 50:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}.")


