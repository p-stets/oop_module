import settings

from datetime import datetime


class Score(object):

    @staticmethod
    def _create_record(file_location, score, name):
        with open(file_location, 'a+') as file:
            file.write('{player_score} {player_name} {date} / {time}'.format(
                player_score=score,
                player_name=name,
                date=datetime.now().date(),
                time=datetime.now().time(),
            ))

    @classmethod
    def write_score(cls, file_location, player_score, player_name):
        with open(file_location, 'a+') as file:
            if len(file.readlines()) > 0:  # Go to newline if file is not empty
                file.write('\n')
            cls._create_record(
                file_location=file_location,
                score=player_score,
                name=player_name
            )

    @classmethod
    def write_best_score(cls, file_location, player_score, player_name):
        with open(file_location, 'a+') as file:
            file_list = file.readlines()
            print('YOOO', len(file_list))
            if 0 < len(file_list) < 10:  # Go to newline if file is not empty
                file.write('\n')
                cls._create_record(
                    file_location=file_location,
                    score=player_score,
                    name=player_name
                )
                results = file_list.sort(reverse=True)
                file.truncate()
                file.writelines(["%s\n" % item for item in results.sort().reverse()])
            else:
                file.write('\n')
                cls._create_record(
                    file_location=file_location,
                    score=player_score,
                    name=player_name
                )
                results = file.readlines().sort(reverse=True)
                if len(results) > 0:
                    file.truncate()
                    results = results[0:len(results) - 1]
                file.writelines(["%s\n" % item for item in results])


class GameOver(Exception, Score):
    pass


class EnemyDown(Exception, Score):
    pass
