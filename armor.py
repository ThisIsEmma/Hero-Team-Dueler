from random import randint

class Armor:
    def __init__(self, armor_name, max_block):
        '''Instantiate instance properties.
        name: String
        max_block: Integer'''
        self.armor_name = armor_name
        self.max_block = max_block

    def block(self):
        ''' Return a value between 0 and the value set by self.max_block.'''
        return randint(0, self.max_block)


if __name__ == "__main__":
    shield = Armor('Shield of discernment', 10)
    print(shield.armor_name)
    print(shield.block())