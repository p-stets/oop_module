import os
import settings

from datetime import datetime
from collections import OrderedDict


class Score(object):

    '''
    File I\\O supportive method(s).

    append_new_record - add a new record to a file.
    append_best_score - is a file parser. Parses all the strings and
    uses the first value of each string to sort the file using it.
    '''

    # Apeend a score to a file
    @staticmethod
    # Appending a new score, score value should be first!
    def append_score(file_location, score: int, name):
        # Open file, create new if not exists
        with open(file_location, 'a+') as file:
            score = '{player_score} {player_name} {date} / {time}'.format(
                player_score=score,
                player_name=name,
                date=datetime.now().date(),
                time=datetime.now().time().strftime('%H:%M:%S'),
            )
            # Write newline if the file is not empty
            if os.stat(file_location).st_size:
                score = '\n' + score
            file.write(score)

    @classmethod
    def append_best_score(cls, file_location, score: int, name, line_limit: int = settings.BEST_CORE_FILE_LENGTH):
        cls.append_score(
            file_location=file_location,
            score=score,
            name=name
        )
        with open(file_location, 'a+') as file:
            file.seek(0)  # Go to the beginning of the file

            lines = file.readlines()
            lines = [line.replace('\n', '') for line in lines]  # Get clean lines
            detailed_list = [line.split(' ') for line in lines]

            scores = {}
            for element in detailed_list:
                score_name = int(element[0])
                score_details = ''
                for item in element[1:]:
                    score_details += ' ' + str(item)
                score_details = score_details.strip()
                scores[score_name] = score_details
            scores = OrderedDict(sorted(scores.items()))
            scores = sorted(scores.items(), reverse=True)
            new_list = [f'{key} {value}' for key, value in scores]
            new_list = new_list[0:line_limit]
            new_list[1:] = ['\n' + line for line in new_list[1:]]
            file.truncate(0)
            file.writelines(new_list)


class GameOver(Exception):
    pass


class EnemyDown(Exception):
    pass
