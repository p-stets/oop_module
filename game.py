import settings
from models import Enemy, Player
from exceptions import EnemyDown, GameOver, Score


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
        Score.append_score(
            file_location=settings.SCORES_FILE,
            name=new_player.name,
            score=new_player.score
        )
        Score.append_best_score(
            file_location=settings.BEST_SCORES_FILE,
            name=new_player.name,
            score=new_player.score
        )
        print("You are out of lives, your game is over, looser!\n")
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
