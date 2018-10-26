import sys

from classes.base_class import Glad
from modules.base_mods import yes_or_no

magic = [{'name': 'Fire',  'cost': 40, 'dmg': 180},
         {'name': 'Water', 'cost': 30, 'dmg': 150},
         {'name': 'Earth', 'cost': 20, 'dmg': 110},
         {'name': 'Air',   'cost': 10, 'dmg': 60},
         {'name': 'Heal',  'cost': 30, 'dmg': 100}]

round_number = 1
level = 1

print('You are sitting in first row of a big arena.\n Crowds are crazy for blood and show, but '
      'no one seems to come on the arena?\n WHOOP.\n You have been pushed down right into the fray'
      ' by member of your own family. Soon gate is opened and tough peasant charges at you.')
input('Press (Enter)')

""" MAIN LOOP
Player chooses option of attack, then based on actions he took resolution is applied to his
HP and MP and enemy HP until one reaches 0 HP
"""
while True:
    """ FIGHT ROUND
    Player chooses action and resolution of that action is applied. Round ends with HP summary.
    """
    if round_number == 1:  # New game generation
        player = Glad(460, 60, 60, magic)
        enemy = Glad(545 + 5*level, 0, 60, [])

    print('=' * 79)
    print('Player HP ', player.hp, '| MP', player.mp)  # Prints HP MP stats of player & enemy
    print('Enemy  HP ', enemy.hp, '\n' + '=' * 79)

    user_input = player.print_actions()  # Print actions and returns correct user input (index of action as integer)

    if user_input == 0:  # attacking
        print('You strike the enemy for ', enemy.reduce_hp(player.attack_damage()),
              'he retaliates with ', player.reduce_hp(enemy.attack_damage()))
    elif user_input == 1:  # casing spell

        while True:  # user cast spell resolution

            print('='*79)
            print('Choose your spell:')  # Player spells
            player.print_magic()
            user_input = input()

            if user_input not in [str(item) for item in range(len(player.magic))]:  # input err handler
                continue

            user_input = int(user_input)

            if player.mp < player.magic[user_input]['cost']:
                print('-'*34+'Not enough MP !!!'+'-'*(79-17-35))
                break

            player.mp -= player.magic[user_input]['cost']  # Decrease player MP by amount cast

            if player.magic[user_input]['name'] == 'Heal':  # Casting heal spell
                print('test OK')
                amount_healed = player.spell_damage(user_input)
                player.hp += amount_healed
                print('Player heals himself for ' + str(amount_healed))
                break

            print('Player casts', player.magic[user_input]['name'], 'for',
                  enemy.reduce_hp(player.spell_damage(user_input)),
                  'damage. Enemy retaliates with',
                  player.reduce_hp(enemy.attack_damage()))
            break

    while player.hp == 0 or enemy.hp == 0:  # End game conditions
        print('The fight lasted %d rounds' % round_number)
        if player.hp > 0:
            print('The enemy is dead. You have win')
        elif enemy.hp > 0:
            print('You are dead. You have lost.')
        else:
            print('The enemy is dead. Who is left to be happy? That is a draw.')

        print('=' * 79)
        print('Player HP ', player.hp, '| MP', player.mp)  # Prints HP MP stats of player & enemy
        print('Enemy  HP ', enemy.hp, '\n' + '=' * 79)
        print('New game? (y)es or (n)o')
        new_game = yes_or_no()
        if new_game == 'yes':
            level += 1
            print('Soon gate is opened and tougher one charges at you.')
            round_number = 0
            break
        else:
            sys.exit()

    round_number += 1
