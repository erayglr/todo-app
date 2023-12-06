import random
import hangman_words
from Beginner.Projects.Hangman import hangman_art

chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
print("Psst, the solution is {}".format(chosen_word))
display = []
for i in range(0, len(chosen_word)):
    display.append("_")
end_of_Game = False
lives = 6
stages = hangman_art.stages
lettersThatSaid = []

while not end_of_Game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You've already guessed {}".format(guess))
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        print("You guessed {}, that's not in the word. You lose a life.".format(guess))
        lettersThatSaid.append(guess)
        print("The letters that you said are : {}".format(lettersThatSaid))
        lives -= 1
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_Game = True
        print("You win")
    if lives == 0:
        end_of_Game = True
        print("You lose")
    print(stages[lives])
