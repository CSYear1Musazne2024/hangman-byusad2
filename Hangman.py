'''Implement your solution in this file.
Make sure that you decompose your solution into appropriate 
functions and that you include appropriate documentation.'''
import random
import string
def load_words():
    try:
        with open('words.txt', 'r') as file:
            words = file.readlines()
        return [word.strip() for word in words]
    except FileNotFoundError:
        print("The words.txt file was not found.")
        exit()
def display_word(secret_word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '-' for letter in secret_word])


def is_valid_guess(guess, guessed_letters):
    return len(guess) == 1 and guess.isalpha() and guess not in guessed_letters
def hangman():
    words = load_wor
    secret_word = random.choice(words).lower()
    guessed_letters = set()
    remaining_guesses = 10
    warnings = 3
    vowels = "aeiou"
    unique_letters = set(secret_word)

    print("Welcome to Hangman!")
    print("I have selected a word. It has", len(secret_word), "letters.")

    while remaining_guesses > 0:
        print("\n--- New Round ---")
        print("Guessed word:", display_word(secret_word, guessed_letters))
        print(f"Guesses remaining: {remaining_guesses}")
        print(f"Warnings remaining: {warnings}")
        print("Letters not guessed yet:", "".join([letter for letter in string.ascii_lowercase if letter not in guessed_letters]))

        # Take user input
        guess = input("Please guess a letter: ").lower()

        # Check for valid input
        if not is_valid_guess(guess, guessed_letters):
            if not guess.isalpha():
                if warnings > 0:
                    warnings -= 1
                    print(f"Invalid input! You have {warnings} warnings left.")
                else:
                    remaining_guesses -= 1
                    print("Invalid input! You lose a guess!")
            else:
                print(f"You already guessed the letter {guess}.")
                if warnings > 0:
                    warnings -= 1
                    print(f"You lose a warning! You have {warnings} warnings left.")
                else:
                    remaining_guesses -= 1
                    print("You lose a guess!")
            continue
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good guess: {guess} is in the word!")
        else:
            if guess in vowels:
                remaining_guesses -= 2
                print(f"Sorry, {guess} is not in the word. You lose 2 guesses!")
            else:
                remaining_guesses -= 1
                print(f"Sorry, {guess} is not in the word. You lose 1 guess!")
        if set(secret_word).issubset(guessed_letters):
            print(f"Congratulations, you've guessed the word: {secret_word}")
            score = remaining_guesses * len(unique_letters)
            print(f"Your score is: {score}")
            break
    if remaining_guesses == 0:
        print(f"You've run out of guesses. The word was: {secret_word}")
        print("Game Over!")
if __name__ == "__main__":
    hangman()
