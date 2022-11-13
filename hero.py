from random import randint
import random
from ability import Ability
from armor import Armor
from weapon import Weapon

# Hero class 

class Hero:
    def __init__(self, hero_name, starting_health = 100):
        '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        self.hero_name = hero_name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills
    
    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Refactor this method to update the following:
        # 1) the number of kills the hero (self) has when the opponent dies.
        # 2) then number of kills the opponent has when the hero (self) dies
        # 3) the number of deaths of the opponent if they die    in the fight
        # 4) the number of deaths of the hero (self) if they die in the fight

        if(len(self.abilities) == 0 and len(opponent.abilities) == 0):
            print('DRAW! No one has abilities')
        else:
            fighting = True
            loop_counter = 0

            while fighting == True:
                hero_damage = self.attack()
                opponent_damage = opponent.attack()
                self.take_damage(opponent_damage)
                opponent.take_damage(hero_damage)
                print(loop_counter)

                if(not opponent.is_alive()):
                    print(f"{self.hero_name} won!")
                    self.add_kill(1)
                    opponent.add_death(1)
                    fighting = False
                elif(not self.is_alive()):
                    print(f"{opponent.hero_name} won!")
                    opponent.add_kill(1)
                    self.add_death(1)
                    fighting = False
                    

        
    def add_weapon(self, weapon):
        ''' Add weapon to abilities list
        '''
        self.abilities.append(weapon)
        

    def add_ability(self, ability):
        ''' Add ability to abilities list
            Ability: Ability Object
        '''
        self.abilities.append(ability)

    def add_armor(self, armor):
        ''' Add armor to armor list
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total_damage:Int'''
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        block = 0
        if (len(self.armors) == 0 or self.current_health == 0):
            print(f'{self.hero_name} is defenseless!')
        else:
            for armor in self.armors:
                block += armor.block()
        return block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        net_damage = damage - self.defend()
        if net_damage >= 0:   
            self.current_health -= net_damage
        print(f'took {damage} damage, net damage: {net_damage}')
        print(f"{self.hero_name} current health is {self.current_health}/{self.starting_health}")

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if(self.current_health > 0): 
            return True
        else:
            return False



# run from the termina;

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

