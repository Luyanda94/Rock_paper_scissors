import random

def get_user_choice():
    print("Choose Rock, Paper, or Scissors:")
    user_choice = input().capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors:")
        user_choice = input().capitalize()
    return user_choice

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
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result, computer_choice = determine_winner(user_choice, computer_choice)
    
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    print(result)

if __name__ == "__main__":
    play_game()
