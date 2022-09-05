import random
from MarkovChain import Markov_Chain

markov_chain = Markov_Chain()


def get_computer_choice(player_last_move):
    # possible_moves = ["rock", "paper", "scissors"]
    # return random.choice(possible_moves)

    choice = markov_chain.computer_next_move(player_last_move)

    return choice


def update_matrix(player_last, player_current):
    if player_last is not None:
        markov_chain.update_matrix(player_last, player_current)


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
