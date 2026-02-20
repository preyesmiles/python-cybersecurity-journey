import random

print("Welcome to the Hangman Challenge")

# Step 1: Choose a random word
wordlist = ["apple", "banana", "cherry"]
chosen_word = random.choice(wordlist)

# Step 2: Create a display list with "_"
display = ["_" for _ in chosen_word]

# Step 3: Set total number of lives
total_lives = 5
lives = total_lives

# Step 4: Keep track of letters guessed
guessed_letters = set()

print(f"You have {total_lives} lives. Try to guess the word!")

# Step 5: Show initial blanks
print(" ".join(display))  # e.g., "_ _ _ _ _"

# Step 6: Main game loop
while True:
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.")
        continue

    # Check if guess was already made
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue
    else:
        guessed_letters.add(guess)

    # Check if guessed letter is in the word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter
        print("Correct guess!")
    else:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

    # Show current state of the word
    print(" ".join(display))

    # Check if player won
    if "_" not in display:
        print("Congratulations! You guessed the word:", chosen_word)
        break

    # Check if player lost
    if lives == 0:
        print("You lost! The word was:", chosen_word)
        break