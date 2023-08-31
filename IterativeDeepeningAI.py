import math

import chess
from AlphaBetaAI import AlphaBetaAI

class IterativeDeepeningAI:
    def __init__(self, depth, color):
        self.limit = depth
        self.color = color
        self.alpha_beta = AlphaBetaAI(depth, color)

    def choose_move(self, board):
        move = self.iterative_deepening(board)
        return move

    def iterative_deepening(self, board):
        # implement iterative deepening using alpha-beta
        best_v = - math.inf
        move = None
        for d in range(self.limit):
            val, next_move = self.alpha_beta.alpha_beta(board, -math.inf, math.inf)
            if val > best_v:
                best_v = val
                move = next_move
        return move
