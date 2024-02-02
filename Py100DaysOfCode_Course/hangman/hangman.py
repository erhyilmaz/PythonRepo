
import random
from hangman_words import word_list
from hangman_art import logo, stages, win_msg, lost_msg

# Choose a random word from the list which will be guessed
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Hang-man game has 6 lives
lives = 6

# Print game logo
print(logo)

# Testing code
# print(f"Debug, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"


end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")

    # Check the guessed letter
    for position in range(word_length):
        # Fill in the display positions with the right guess
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    # Check if user guess is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print(lost_msg)

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(stages[lives])
        print(win_msg)

