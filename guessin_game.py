import random

# Words according to difficulty
easy_words = ["cat", "dog", "sun", "book"]
medium_words = ["python", "laptop", "flower", "garden"]
hard_words = ["elephant", "diamond", "umbrella", "computer"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter difficulty: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
max_attempts = 5

print("\nGuess the secret password")

while attempts < max_attempts:

    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

    else:
        hint = ""

        for i in range(len(secret)):
            if i < len(guess) and guess[i] == secret[i]:
                hint += guess[i]
            else:
                hint += "_"

        print("Hint:", hint)
        print("Attempts remaining:", max_attempts - attempts)

else:
    print("Game over!")
    print("The correct password was:", secret)