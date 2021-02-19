import random
import settings

from exceptions import EnemyDown, GameOver


class Enemy(object):

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return random.choice(settings._ALLOWED_ATTACKS)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise EnemyDown


class Player(object):

    def __init__(self, name, lives=settings.PLAYER_LIVES, allowed_attacks=settings._ALLOWED_ATTACKS):
        self.name = name
        self.lives = lives
        self.score = 0
        self.allowed_attacks = allowed_attacks

    # Get results using results matrix
    @staticmethod
    def fight(attack: int, defence: int):
        return settings.FIGHT_RESULTS[attack][defence]

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver

    def attack(self, enemy_obj):
        player_value = int(input(
            'Input your attack 1,2 or 3\n'
            '1 for Wizard\n'
            '2 for Warrior\n'
            '3 for Mugger\n'
        ))
        enemy_value = enemy_obj.select_attack()
        if player_value not in self.allowed_attacks:
            print(f'Wrong value of {player_value}, try again\n')
            self.attack(enemy_obj)
        result = self.fight(player_value, enemy_value)
        if result == 0:
            print(
                'It\'s a draw!\n'
                f'Your enemy got {enemy_value}\n'
            )
        elif result == 1:
            enemy_obj.decrease_lives()
            self.score += 1
            print(
                'You attacked successfully!\n'
                f'Your enemy got {enemy_value}\n'
            )
        else:
            print(
                'You missed!\n'
                f'Your enemy got {enemy_value}\n'
            )

    def defence(self, enemy_obj):
        player_value = int(input(
            'Input your defence 1,2 or 3\n'
            '1 for Wizard\n'
            '2 for Warrior\n'
            '3 for Mugger\n'
        ))
        enemy_value = enemy_obj.select_attack()
        if player_value not in self.allowed_attacks:
            print(f'Wrong value of {player_value}, try again\n')
            self.attack(enemy_obj)
        result = self.fight(enemy_value, player_value)
        if result == 0:
            print(
                'It\'s a draw!\n'
                f'Your enemy got {enemy_value}\n'
            )
        elif result == 1:
            self.decrease_lives()
            print(
                'You were hit!\n'
                f'Your enemy got {enemy_value}\n'
            )
        else:
            print(
                'Your defence was successfull!\n'
                f'Your enemy got {enemy_value}\n'
            )
