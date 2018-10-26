# functions


def yes_or_no():  # Returns 'yes' or 'no' based on first letter of user input.

    while True:
        item = input()
        if not item or item[0] not in ['y', 'n']:
            print('(y)es or (n)o are valid answers')
            continue
        elif item[0].lower() == 'y':
            return 'yes'
        elif item[0].lower() == 'n':
            return 'no'
