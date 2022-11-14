from random import randint
from ability import Ability

class Weapon(Ability):
    def __init__(self, ability_name, max_damage):
        super().__init__(ability_name, max_damage)

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return randint(self.max_damage // 2, self.max_damage) 

if __name__ == '__main__':
    baton_rouge = Weapon('Baton magic', 100)
    print(baton_rouge.attack())