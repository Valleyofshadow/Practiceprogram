import random
import os
clear = lambda: os.system('cls')


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
words = [
'abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
]
keyword = words[random.randrange(0, len(words))]
trys = 6
i = 0
current = '_'
guesses = []
print (logo)
while i < len(keyword)-1:
    current = current + "_"
    i = i + 1
def hangman(x):
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    return (stages[x])



def test(y):
    t = 0
    for x in keyword:
        if y == x:
            t = 1
    if t == 1:
        return 1
    elif t == 0:
        return 0


def update(current, keyword,y):
    i = 0
    while i < len(keyword):
        if y == keyword[i]:
            if i == 0:
                stop = i + 1
                current = y + current[stop:]
            elif i == len(keyword)-1:
                current = current[:i] + y
            else:
                start = i
                stop = i + 1
                current = current[:start] + y + current[stop:]
        i = i + 1
    return current


while trys > 0:
    #clear()
    print (logo)
    print (hangman(trys))
    print(current, "(", len(keyword),")")
    print(guesses)
    guess = input('Guess a letter\n').lower()
    state = test(guess)
    if state == 1:
        current = (update(current, keyword, guess))
    elif state == 0:
        trys = trys - 1
        print (guess + " is not in the word")
        print ("Lives remaining: " + str(trys))
        guesses.append(guess)
    if "_"  not in current:
        print ('You win')
        print (current)
        break
if trys == 0:
    print (hangman (0))
    print ("You lost")
    print (current)
    print (keyword)
input()
