from random import randint
import random


class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        fighters = [self.name, opponent.name]
        winner = random.choice(fighters)
        fighters.remove(winner)
        print(f'{winner} obliterates {fighters[0]}!')


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  my_hero = Hero("Grace Hopper", 200)
  their_hero = Hero("Alexander the great", 200)
  print(my_hero.name)
  print(my_hero.current_health)
  my_hero.fight(their_hero)

