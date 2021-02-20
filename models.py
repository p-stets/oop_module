import random
import settings
# from pprint import pprint as output

from exceptions import EnemyDown, GameOver


class Enemy(object):

    '''
    An enemy class
    '''

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return random.choice(settings._ALLOWED_ATTACKS)

    def decrease_lives(self):
        self.lives -= 1
        print('Enemy lives: ', self.lives)
        if self.lives <= 0:
            print('Enemy down!')
            raise EnemyDown


class Player(object):

    '''
    A player class
    '''

    score = 0

    def __init__(self, name, lives=settings.PLAYER_LIVES, allowed_attacks=settings._ALLOWED_ATTACKS):
        self.name = name
        self.lives = lives
        self.allowed_attacks = allowed_attacks

    @staticmethod
    def commands(
        action,
        best_scores_file=settings.BEST_SCORES_FILE,
        scores_file=settings.SCORES_FILE,
        allowed_commands=settings.ALLOWED_COMMANDS
    ):
        def print_file(location):
            with open(location, 'r') as file:
                lines = file.readlines()
                lines = [line.replace('\n', '') for line in lines]
                print('\n'.join(lines))

        if action == 'help':
            print(f'Allowed commands are: {allowed_commands}')
        elif action == 'show scores':
            print_file(location=settings.SCORES_FILE)
        elif action == 'show best scores':
            print_file(location=settings.BEST_SCORES_FILE)
        elif action == 'exit':
            raise KeyboardInterrupt

    @classmethod
    def player_int_input(cls, allowed_list=settings._ALLOWED_ATTACKS, allowed_commands=settings.ALLOWED_COMMANDS):
        while True:
            try:
                value = input('\nMake your Choice:').lower()
                if value in allowed_commands:
                    Player.commands(value)
                    continue
                else:
                    if int(value) not in allowed_list:
                        raise ValueError
            except ValueError:
                print(f'Wrong value of {value}, try again')
                continue
            else:
                return int(value)

    # Get results using results matrix
    @staticmethod
    def fight(attack: int, defence: int):
        return settings.FIGHT_RESULTS[attack][defence]

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver

    def attack(self, enemy_obj):
        print(
            '\nInput your attack 1,2 or 3'
            '\n1 for Wizard'
            '\n2 for Warrior'
            '\n3 for Mugger'
        )
        player_attack_value = Player.player_int_input(settings._ALLOWED_ATTACKS)
        enemy_value = enemy_obj.select_attack()
        result = self.fight(player_attack_value, enemy_value)
        if result == 0:
            print(
                'It\'s a draw!\n'
                f'Your enemy got {enemy_value}'
            )
        elif result == 1:
            print(
                'You attacked successfully!\n'
                f'Your enemy got {enemy_value}'
            )
            enemy_obj.decrease_lives()
            self.score += 1
        else:
            print(
                'You missed!\n'
                f'Your enemy got {enemy_value}'
            )

    def defence(self, enemy_obj):
        print(
            '\nInput your defence 1,2 or 3'
            '\n1 for Wizard'
            '\n2 for Warrior'
            '\n3 for Mugger'
        )
        player_defence_value = Player.player_int_input(settings._ALLOWED_ATTACKS)
        enemy_value = enemy_obj.select_attack()
        result = self.fight(enemy_value, player_defence_value)
        if result == 0:
            print(
                'It\'s a draw!\n'
                f'Your enemy got {enemy_value}'
            )
        elif result == 1:
            self.decrease_lives()
            print(
                'You were hit!\n'
                f'Your enemy got {enemy_value}'
            )
        else:
            print(
                'Your defence was successfull!\n'
                f'Your enemy got {enemy_value}'
            )
