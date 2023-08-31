# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame


import sys


# player1 = HumanPlayer()
# player2 = RandomAI()
player1 = MinimaxAI(500, 0)
player2 = AlphaBetaAI(500, 1)

# game = ChessGame(player1, player2)
game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()


#print(hash(str(game.board)))
