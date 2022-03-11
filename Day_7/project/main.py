import  random
from hangman_words import word_list
from hangman_art import  logo, stages
list_of_words = word_list

chosen_word = random.choice(list_of_words)
blanck_word = ""

for _ in chosen_word:
    blanck_word += "_"

word_sicret = list(blanck_word)
end_of_game = False
lives = 6
stages = stages

print(logo)
print(chosen_word)

while not end_of_game:
    guess = input("Guess a letter in the word: ").lower()

    if guess in word_sicret:
        print(f"You've already Guess {guess}")

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            letter = chosen_word[index]

            if letter == guess:
                word_sicret[index] = guess
        if "_" not in word_sicret:
            print("YOU WIN")
            end_of_game = True
    else:
        print(f"You guessed the latter {guess}, that's not in the word, YOU LOSE A LIFE")
        lives -=  1
        print(stages[lives])

        if lives == 0:
            print("You lose, Game Over")
            end_of_game = True
    print(f"".join(word_sicret))