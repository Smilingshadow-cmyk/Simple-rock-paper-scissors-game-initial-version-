def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"

    if user_choice == "rock" and computer_choice == "scissors":
        return "user"

    if user_choice == "paper" and computer_choice == "rock":
        return "user"

    if user_choice == "scissors" and computer_choice == "paper":
        return "user"

    return "computer"
