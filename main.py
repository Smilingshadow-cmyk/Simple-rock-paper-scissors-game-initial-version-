from get_computer_choice import get_computer_choice
from get_winner import get_winner
from load_score import load_score
from print_score import print_score
from save_score import save_score


def play_new_game():
    score = load_score()

    print("\nNew Game Started!")
    print("Type rock, paper, or scissors.")
    print("Type 4 to stop this game and go back to the menu.\n")

    while True:
        user_choice = input("Your choice: ").lower().strip()

        if user_choice == "4":
            save_score(score)
            print("\nGame saved.")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please type rock, paper, scissors, or 4.")
            continue

        computer_choice = get_computer_choice()
        winner = get_winner(user_choice, computer_choice)

        print(f"Computer chose: {computer_choice}")

        if winner == "user":
            print("You win this round!")
            score["wins"] += 1
        elif winner == "computer":
            print("Computer wins this round!")
            score["losses"] += 1
        else:
            print("It is a tie!")
            score["ties"] += 1

        save_score(score)
        print_score(score)


def show_menu():
    while True:
        print("\n===== Rock Paper Scissors =====")
        print("1. New Game")
        print("2. Old Score")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_new_game()
        elif choice == "2":
            score = load_score()
            print_score(score)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid menu option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    show_menu()
