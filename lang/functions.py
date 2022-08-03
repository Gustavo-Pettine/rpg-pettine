from codecs import lookup_error
from lang.player import Player

def print_player(player: "Player"):
  player.print()

def load(name=None):
  return Player(name=name)

def battle(player_1: "Player", player_2: "Player"):
  Player.battle(player_1=player_1, player_2=player_2)

def select_from(property: str, player: "Player"):
  try:
    print(player[property])

  except LookupError:
    print(f'undefined property {property}')
  