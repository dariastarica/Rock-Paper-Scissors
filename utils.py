import random

players_choices_list = []


def get_computer_choice():
    possible_moves = ["rock", "paper", "scissors"]
    return random.choice(possible_moves)
    # players_choices_list.append(last_player_choice)


def decide_winner(players_choice, computer_choice):
    if players_choice == computer_choice:
        return "It's a draw"
    elif players_choice == "rock":
        if computer_choice == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif players_choice == "paper":
        if computer_choice == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif players_choice == "scissors":
        if computer_choice == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
