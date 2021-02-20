# Number of player lives
PLAYER_LIVES = 1

# Hero classes and names
HERO_CLASSES = {
    'WIZARD': {
        'VALUE': 1,
        'NAME': 'Wizard'
    },
    'WARRIOR': {
        'VALUE': 2,
        'NAME': 'Warrior'
    },
    'MUGGER': {
        'VALUE': 3,
        'NAME': 'Mugger'
    }
}

# File with regular scores (log)
SCORES_FILE = 'scores.txt'

# File with the best scores ever
BEST_SCORES_FILE = 'best_scores.txt'

# Number of max lines for best crores file
BEST_CORE_FILE_LENGTH = 10

# List of values for every hero class
_ALLOWED_ATTACKS = [int(i['VALUE']) for i in HERO_CLASSES.values()]

# Results matrix; use Row > Column (Attack > Defence)
FIGHT_RESULTS = [
    [0, 1, 2, 3],
    [1, 0, 1, -1],
    [2, -1, 0, 1],
    [3, 1, -1, 0]
]

# Additional allowed commands
ALLOWED_COMMANDS = [
    'show scores',
    'show best scores',
    'help',
    'exit'
]
