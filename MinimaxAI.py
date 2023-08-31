import math
import random

import chess

class MinimaxAI():
    def __init__(self, depth, color):
        self.limit = depth
        self.curr_depth = 0
        self.color = color
        # update curr_depth during the search

    def choose_move(self, board):       # minimax decision
        # before calling minimax, reset curr_depth to 0
        self.curr_depth = 0
        v, move = self.minimax(board)
        # print(move)
        print("Minimax AI recommending move " + str(move))
        return move

    def minimax(self, board):
        if board.turn == self.color:
            self.curr_depth += 1
            return self.max_value(board)        # if next agent is max
        else:
            self.curr_depth += 1
            return self.min_value(board)

    def min_value(self, board):
        # terminal test
        if self.cutoff_test(board):
            return self.evalutaion(board), None
        v = math.inf
        moves = list(board.legal_moves)
        random.shuffle(moves)
        best_move = moves[0]
        for move in moves:
            board.push(move)
            successor_val = self.minimax(board)[0]
            if v < successor_val:
                v = successor_val
                best_move = move
            board.pop()
        return v, best_move

    def max_value(self, board):
        if self.cutoff_test(board):
            return self.evalutaion(board), None
        v = - math.inf
        moves = list(board.legal_moves)
        random.shuffle(moves)
        best_move = moves[0]
        for move in moves:
            board.push(move)
            successor_val = self.minimax(board)[0]
            if v > successor_val:
                v = successor_val
                best_move = move
            board.pop()
            # update best move
        return v, best_move

    def evalutaion(self, board):
        # return the material value of the board
        # check if is checkmate
        if board.is_checkmate():
            if board.outcome().winner == self.color:
                return math.inf
            else:
                return -math.inf

        side = board.turn
        material_value = 0
        piece_val = {chess.PAWN: 1, chess.KNIGHT: 4, chess.BISHOP: 5, chess.ROOK: 6, chess.QUEEN: 10, chess.KING: 100}
        for t, val in piece_val.items():
            material_value += len(board.pieces(t, side)) * val
        return material_value

    def cutoff_test(self, board):
        if board.is_game_over() or self.curr_depth >= self.limit:
            return True
        else:
            return False