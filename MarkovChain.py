import random as rm


def init_matrix():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return matrix


class Markov_Chain:
    def __init__(self):
        self.lose_combo = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
        self.matrix = init_matrix()
        self.matrix_index = {"rock": 0,
                             "paper": 1,
                             "scissors": 2}

    def update_matrix(self, prev_move, next_move):
        self.matrix[self.matrix_index[prev_move]][self.matrix_index[next_move]] = \
            self.matrix[self.matrix_index[prev_move]][self.matrix_index[next_move]] + 1

    def computer_next_move(self, prev_move):
        # if this is the first move, the computer chooses at random
        if prev_move is None:
            return rm.choice(["rock", "paper", "scissors"])
        else:
            '''
            if there are previous player moves stored in the matrix, the computer computes the most probable move of the 
            player based on the matrix.
            '''
            next_move = max(self.matrix[self.matrix_index[prev_move]])
            predicted_next_move = list(self.matrix_index.keys())[list(self.matrix_index.values()).index(next_move)]

        return self.lose_combo[predicted_next_move]
