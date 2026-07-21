import random

words = ["python", "codealpha", "developer", "program", "hangman"]

def main():
    secret_word = random.choice(words)
    guessed = []
    lives = 6

   
    print(f"Welcome to Hangman!\nTry to guess the word letter by letter.")

    while lives > 0:
        display = ""
        for char in secret_word:
            if char in guessed:
                display += char + " "
            else:
                display += "_ "
      
        guessed_str = ", ".join(guessed) if guessed else "None"
        print(f"\nWord: {display}\nLives left: {lives}\nGuessed letters: {guessed_str}")

        if "_" not in display:
            print(f"\nYou win! The word was: {secret_word}")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed:
            print(f"You already guessed '{guess}'!")
            continue

        guessed.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    if lives == 0:
        print(f"\nGame over! Out of tries. The word was: {secret_word}")

if __name__ == "__main__":
    main()
