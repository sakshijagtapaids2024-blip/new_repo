import random

print("🎮 Welcome to the Number Guessing Game!")

secret = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        print("🎉 Congratulations! You guessed it correctly.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0 and guess != secret:
    print(f"😔 You lost! The correct number was {secret}.")