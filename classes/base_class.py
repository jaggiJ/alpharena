import random


class Glad:
    def __init__(self, hp, mp, atk, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk = atk
        self.magic = magic
        self.actions = ['Melee', 'Magic']

    def attack_damage(self):
        return random.randint(self.atk-10, self.atk+10)

    def spell_damage(self, i):
        dmgl = self.magic[i]['dmg'] - 10
        dmgh = self.magic[i]['dmg'] + 10
        return random.randint(dmgl, dmgh)

    def reduce_hp(self, dmg):  # decreases hp by input, returns updated hp
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return dmg

    def reduce_mp(self, mp_cost):
        self.mp -= mp_cost
        if self.mp < 0:
            self.mp = 0
        return self.mp

    def print_actions(self):
        """
        prints all actions available, returns index of user chosen action

        user_input  - desired user input is number in range of available player actions
        item        - instance of action available to user
        """
        print('Chose your action:')
        for item in self.actions:
            print(self.actions.index(item), item)
        while True:
            user_input = input()
            if user_input not in [str(item) for item in range(len(self.actions))]:  # input err handler
                print('Write number addressing action you desire')
                continue
            else:
                break
        return int(user_input)

    def print_magic(self):  # prints all spells available
        for item in self.magic:
            print(self.magic.index(item), end=' ')
            print(str(item)[1:-1].lstrip("'name: "))
