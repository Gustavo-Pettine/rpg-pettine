import random, os, time

NAMES = [
  "JOAO",
  "CARLOS",
  "GUSTAVO",
  "PETTINE",
  "ALBERTO",
  "HENRIQUE",
  "ALESSANDRO",
]

TECHNIQUES = [
  "SOCO DE DIREITA",
  "SOCO CRUZADO",
  "CHUTE RODADO",
  "JOELHADA NA BARRIGA",
]

ATTACK_CHANCES = [
  "Errou!",
  "Acertou!",
  "Acerto Crítico!",
]

class Player:
  def __init__(self, name=None) -> None:
    random_name = f"{random.choice(NAMES)} {random.choice(NAMES)}"

    self.name = random_name if name == None else name
    self.health_points = random.random()*100
    self.attack = random.random()*100
    self.defense = random.random()*100
    self.speed = random.random()*100
  
  def __getitem__(self, key):
    return getattr(self, key)

  def print(self):
    print("----------")
    print(f"nome: {self.name}")
    print(f"HP: {self.health_points:.2f}")
    print(f"Ataque: {self.attack:.2f}")
    print(f"Defesa: {self.defense:.2f}")
    print(f"Velocidade: {self.speed:.2f}")
    print("----------")

  @staticmethod
  def attack_player(player_to_attack: "Player", player_to_defend: "Player"):
    attack_name = random.choice(TECHNIQUES)
    attack_message = f"{player_to_attack.name} ataca {player_to_defend.name} com {attack_name}!"
    attack_effectiveness = random.choice(ATTACK_CHANCES)
    attack_damage = (player_to_attack.attack / player_to_defend.defense) * ATTACK_CHANCES.index(attack_effectiveness) * (1 + random.random() / 2)
    
    dodged = random.random() >  (player_to_attack.speed / player_to_defend.speed)
    if dodged: attack_damage = 0

    print(attack_message)
    print(attack_effectiveness)
    if dodged: print(f"{player_to_defend.name} desviou!")
    print(f"{player_to_defend.name} tomou {attack_damage:.2f} de dano!")
    player_to_defend.health_points -= attack_damage

    if (player_to_defend.health_points < 0):
      print(f"{player_to_defend.name} foi pro saco!")

  @staticmethod
  def battle(player_1: "Player", player_2: "Player"):
    turn_number = 0
    while player_1.health_points > 0 and player_2.health_points > 0:
      turn_number += 1
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f"Turno: {turn_number}")
      player_1.print()
      player_2.print()
      print("\n\n")
      Player.attack_player(player_1, player_2)
      print("\n\n")
      Player.attack_player(player_2, player_1)
      time.sleep(2)