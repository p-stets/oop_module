from models import Enemy, Player
import settings
from exceptions import EnemyDown, GameOver


player_name = str(input('What is your name?\n'))

new_player = Player(
    name=player_name,
    lives=settings.PLAYER_LIVES
)
level = 1
new_enemy = Enemy(level)


def play(new_player=new_player, level=level, new_enemy=new_enemy):
    while True:
        try:
            new_player.attack(new_enemy)
            new_player.defence(new_enemy)
        except EnemyDown:
            level += 1
            new_player.score += 5
            new_enemy = Enemy(level)
            new_enemy.level += 1


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        GameOver.write_score(
            file_location=settings.SCORES_FILE,
            player_name=new_player.name,
            player_score=new_player.score
        )
        GameOver.write_best_score(
            file_location=settings.BEST_SCORES_FILE,
            player_name=new_player.name,
            player_score=new_player.score
        )
        print("Game over, looser!\n")
    except EnemyDown:
        print("Enemy down!\n")
    except KeyboardInterrupt:
        pass
