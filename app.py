import random

def play_rock_paper_scissors():
    user_score = 0
    computer_score = 0

    while True:
        user_input = input("Enter a choice (rock, paper, scissors): ")
        user_choice = user_input.lower()
        possible_actions = ["rock", "paper", "scissors"]
        
        if user_choice not in possible_actions:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(possible_actions)
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print("Both players selected the same. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
                user_score += 1
            else:
                print("Paper covers rock! You lose.")
                computer_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose.")
                computer_score += 1

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            print(f"\nFinal Scores:\nYou: {user_score}\nComputer: {computer_score}")
            break

if __name__ == "__main__":
    play_rock_paper_scissors()