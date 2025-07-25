import random

# Map choices to symbols (emojis)
symbols = {
    'rock': '✊',
    'paper': '✋',
    'scissors': '✌️'
}

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Choose rock (✊), paper (✋), or scissors (✌️): ").strip().lower()
        if user_input in choices:
            return user_input
        print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    # Debug print (comment out if not needed)
    # print(f"DEBUG: user={user}, computer={computer}")

    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user} {symbols[user]}")
    print(f"Computer chose: {computer} {symbols[computer]}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    print("=== Rock, Paper, Scissors ===")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {computer_score}\n")

        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
