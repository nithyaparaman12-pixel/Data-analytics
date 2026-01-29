import random

print("🎯 Welcome to Secret Number Guessing Game")

while True:
    print("\nChoose Difficulty Level")
    print("1. Easy (1 to 10, 5 attempts)")
    print("2. Medium (1 to 20, 7 attempts)")
    print("3. Hard (1 to 50, 10 attempts)")

    try:
        level = int(input("Enter your choice (1-3): "))

        if level == 1:
            max_num = 100
            max_attempts = 7
        elif level == 2:
            max_num = 200
            max_attempts = 14
        elif level == 3:
            max_num = 500
            max_attempts = 20
        else:
            print("Invalid level choice")
            continue

        secret_number = random.randint(1, max_num)
        attempts = 0

        print(f"\nGuess the number between 1 and {max_num}")
        print(f"You have {max_attempts} attempts")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess == secret_number:
                    print(f"🎉 Correct! You guessed it in {attempts} attempts")
                    break
                elif guess < secret_number:
                    print("Too low!")
                else:
                    print("Too high!")

            except ValueError:
                print("❌ Please enter a valid number")

        else:
            print(f"😢 Game Over! The number was {secret_number}")

    except ValueError:
        print("❌ Invalid input")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing!")
        break
