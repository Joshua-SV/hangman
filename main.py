import random
import stageArt
import words
import os

# display logo
print(stageArt.logo)

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosenWord = random.choice(words.word_list)

# replace string with blanks then display
display = []
length = len(chosenWord)
endOfgame = False
lives = len(stageArt.stages)
clear = lambda: os.system('clear')

for i in range(length):
    display.append("_")

print(f"{' '.join(display)}")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while not endOfgame:
    guess = input("Enter a letter to guess: ").lower()


    clear()

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    for x in range(length):
        if guess == chosenWord[x]:
            display[x] = guess;

    if guess not in display:
        lives -= 1
        print(stageArt.stages[lives])

    print(f"{' '.join(display)}")

    if "_" not in display:
        endOfgame = True
        print("You Win!!!")
    elif lives == 0:
        endOfgame = True
        print("You Lose!!!")