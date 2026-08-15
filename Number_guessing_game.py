"""
Number Guessing Game
Syntecxhub Week 1 - Project 2
Author: Ananya
Description: Guess a random number with difficulty levels and best score tracking.
"""

import random

def get_difficulty() -> int:
    """Prompt user for difficulty and return max range for the game."""
    print("\n--- Choose Difficulty ---")
    print("1. Easy   - 1 to 50")
    print("2. Medium - 1 to 100")
    print("3. Hard   - 1 to 500")
    choice = input("Enter 1/2/3: ")
    return {'1': 50, '2': 100, '3': 500}.get(choice, 100)

def play_round(max_num: int) -> int:
    """
    Play one round of guessing game.
    Args:
        max_num: Upper limit of the random number.
    Returns:
        Number of attempts taken to guess correctly.
    """
    secret_number = random.randint(1, max_num)
    attempts = 0
    print(f"\nI'm thinking of a number between 1 and {max_num}")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too Low! Go Higher.")
            elif guess > secret_number:
                print("Too High! Go Lower.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                return attempts
        except ValueError:
            print("Please enter a valid integer.")

def play_game() -> None:
    """Main game loop with replay option and best score tracking."""
    best_score = None
    while True:
        max_range = get_difficulty()
        attempts = play_round(max_range)

        # Track best score
        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"🏆 New Best Score: {best_score} attempts!")
        else:
            print(f"Current Best Score: {best_score} attempts")

        replay = input("\nPlay again? y/n: ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_game()
