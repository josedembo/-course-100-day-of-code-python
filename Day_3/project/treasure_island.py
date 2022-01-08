print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

option = input("left or right? ").lower()

if option == "left":
    option_2 = input("swim or wait? ").lower()
    if option_2 == "wait":
        option_3 = input("Which door? red, blue or yellow? ").lower()
        if option_3 == "red":
            print("Burned by fire. Game Over.")
        elif option_3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif option_3 == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")