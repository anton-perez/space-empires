from random import random
import math

class CustomPlayer():
  def __init__(self):
    self.player_number = None

  def set_player_number(self, n):
    self.player_number = n

  def get_opponent_player_number(self):
    if self.player_number == None:
      return None
    elif self.player_number == 1:
      return 2
    elif self.player_number == 2:
      return 1

  def calc_distance(self, point_1, point_2):
    return (abs(point_2[0]-point_1[0])**2 + abs(point_2[1]-point_1[1])**2)**0.5

  def choose_translation(self, game_state, choices, scout_num):
    myself = game_state['players'][self.player_number]
    opponent_player_number = self.get_opponent_player_number()
    opponent = game_state['players'][opponent_player_number]

    my_scout_coords = myself['scout_coords'][scout_num]
    opponent_home_colony_coords = opponent['home_colony_coords']
    if choices != []:
      min_coords = choices[0]
      min_distance = self.calc_distance((my_scout_coords[0] + min_coords[0], my_scout_coords[1] + min_coords[1]), opponent_home_colony_coords)
      for choice in choices:
        current_coords = (my_scout_coords[0] + choice[0], my_scout_coords[1] + choice[1])
        current_distance = self.calc_distance(current_coords, opponent_home_colony_coords)

        if current_distance < min_distance:
          min_distance = current_distance
          min_coords = choice

      return min_coords 
