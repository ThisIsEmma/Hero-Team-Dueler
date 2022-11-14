from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: Team object
            team_two: Team object
        '''
        self.team_one = Team(team_name = input("What will be the first team's name? "))
        self.team_two = Team(team_name = input("What will be the second team's name? "))

    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
        "What is the max damage of the ability?  ")

        return Ability(name, int(max_damage))

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is the weapon name?  ")
        max_damage = input(
        "What is the max damage of the weapon?  ")

        return Weapon(name, int(max_damage))

    def create_armor(self):
        '''Prompt user for Armor information
        return Armor with values from user input.
        '''
        name = input("What is the armor name?  ")
        max_block = input(
        "What is the max block of the armor?  ")

        return Armor(name, int(max_block))

    def create_hero(self):
        '''Prompt user for Hero information
        return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                # TODO add an ability to the hero
                # HINT: First create the ability, then add it to the hero
                hero.add_ability(self.create_ability())

            elif add_item == "2":
                # TODO add a weapon to the hero
                # HINT: First create the weapon, then add it to the hero
                hero.add_weapon(self.create_weapon())

            elif add_item == "3":
                # TODO add an armor to the hero
                # HINT: First create the armor, then add it to the hero
                hero.add_armor(self.create_armor())

        return hero

        # build_team_one is provided to you
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        numOfTeamMembers = int(input(f"How many members would you like on {self.team_one.team_name} team?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers = int(input(f"How many members would you like on {self.team_two.team_name}?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)


    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        # Some help on how to achieve these tasks:
        # TODO: for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        team_one_survivors_count = 0

        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f'team one: {hero.hero_name}  is still alive!')
                team_one_survivors_count += 1

        team_two_survivors_count = 0
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f'team two: {hero.hero_name}  is still alive!')
                team_two_survivors_count += 1
        
        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team

        if team_one_survivors_count > team_two_survivors_count:
            print('Team one won!')
        elif team_one_survivors_count == team_two_survivors_count:
            print('DRAW!')
        else:
            print('Team two won!')

        # TODO for each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team
        
        print("\n")
        print(self.team_one.team_name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.team_name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.team_name + " average K/D was: " + str(team_kills/team_deaths))

        # TODO: Now display the average K/D for Team Two
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.team_name + " average K/D was: " + str(team_kills/team_deaths))

        # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.team_name + ": " + hero.hero_name)

        #TODO: Now list the heroes from Team Two that survived
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.team_name + ": " + hero.hero_name)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()