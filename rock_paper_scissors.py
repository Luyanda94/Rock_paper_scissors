import random

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", computer_choice
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!", computer_choice
    else:
        return "You lose!", computer_choice

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result, computer_choice = determine_winner(user_choice, computer_choice)

        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        print(result)

        if "win" in result.lower():
            user_score += 1
            print(f"You're on fire! Your Score: {user_score} | Computer Score: {computer_score}")
        elif "lose" in result.lower():
            computer_score += 1
            print(f"Better luck next time! Your Score: {user_score} | Computer Score: {computer_score}")
        else:
            print(f"Your Score: {user_score} | Computer Score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
            play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("Thanks for playing. See you next time!")
            break

if __name__ == "__main__":
    play_game()
