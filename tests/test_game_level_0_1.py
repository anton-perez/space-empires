import sys
sys.path.append('games')
from game_level_0_1 import *
sys.path.append('players')
from random_player import *
from custom_player import *

players = [CustomPlayer(), CustomPlayer()]
game = Game(players)
assert game.game_state['players'] == {
    1: {
        'scout_coords': (4, 1),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 7),
        'home_colony_coords': (4, 7)
    }
}

game.complete_movement_phase()
assert game.game_state['players'] == {
    1: {
        'scout_coords': (4, 2),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 6),
        'home_colony_coords': (4, 7)
    }
}

game.complete_combat_phase()

game.complete_movement_phase()
assert game.game_state['players'] == {
    1: {
        'scout_coords': (4, 3),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 5),
        'home_colony_coords': (4, 7)
    }
}

game.complete_combat_phase()

game.complete_movement_phase()
assert game.game_state['players'] == {
    1: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 7)
    }
}

game.complete_combat_phase()

print(game.game_state['players'])

# Possibility 1:
# {
#     1: {
#         'scout_coords': None,
#         'home_colony_coords': (4, 1)
#     },
#     2: {
#         'scout_coords': (4, 4),
#         'home_colony_coords': (4, 7)
#     }
# }

# Possibility 2:
# {
#     1: {
#         'scout_coords': (4, 4),
#         'home_colony_coords': (4, 1)
#     },
#     2: {
#         'scout_coords': None,
#         'home_colony_coords': (4, 7)
#     }
# }


num_wins = {1: 0, 2: 0}
for _ in range(200):
  players = [CustomPlayer(), CustomPlayer()]
  game = Game(players)
  game.run_to_completion()
  winner = game.game_state['winner']
  num_wins[winner] += 1

print(num_wins)