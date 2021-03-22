import sys
sys.path.append('games')
from game_level_0_3 import *
sys.path.append('players')
from random_player import *
from custom_player import *

players = [CustomPlayer(), CustomPlayer()]
game = Game(players, 1)
game.run_to_completion()