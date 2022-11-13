class Team:
    def __init__(self, team_name):
        ''' Initialize your team with its team name and an empty list of heroes'''
        self.team_name = team_name
        self.heroes = list()

    def remove_hero(self, hero_name):
        '''Remove hero from heroes list. If Hero isn't found return 0.'''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.hero_name == hero_name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.hero_name)

    def add_hero(self, hero):
        '''Add a hero to the Hero list
           hero: Hero object'''
        self.heroes.append(hero)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    team = Team("One")
    print(team.team_name)