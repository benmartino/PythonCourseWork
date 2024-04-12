# These are helper functions. I have written them to help make programming easier
# They work just like the built-in functions like print(), int(), round(), ect
# You just call their name and sometimes save what they give you in a variable!
# we will learn how to write our own functions soon
#-----------------------------------------------
# YOU SHOULD NOT MODIFY ANY CODE BEFORE LINE 92 
#-----------------------------------------------
import random
def get_random_word():
    #this function picks a random word to be guessed from a list of valid words
    lis = ['ABOUT', 'ABOVE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY', 'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD', 'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT', 'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT', 'DRAMA', 'DRAWN', 'DREAM', 'DRESS', 'DRILL', 'DRINK', 'DRIVE', 'DROVE', 'DYING', 'EAGER', 'EARLY', 'EARTH', 'EIGHT', 'ELITE', 'EMPTY', 'ENEMY', 'ENJOY', 'ENTER', 'ENTRY', 'EQUAL', 'ERROR', 'EVENT', 'EVERY', 'EXACT', 'EXIST', 'EXTRA', 'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD', 'FIFTH', 'FIFTY', 'FIGHT', 'FINAL', 'FIRST', 'FIXED', 'FLASH', 'FLEET', 'FLOOR', 'FLUID', 'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME', 'FRANK', 'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FULLY', 'FUNNY', 'GIANT', 'GIVEN', 'GLASS', 'GLOBE', 'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT', 'GRASS', 'GREAT', 'GREEN', 'GROSS', 'GROUP', 'GROWN', 'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'HAPPY', 'HARRY', 'HEART', 'HEAVY', 'HENCE', 'HENRY', 'HORSE', 'HOTEL', 'HOUSE', 'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INNER', 'INPUT', 'ISSUE', 'JAPAN', 'JIMMY', 'JOINT', 'JONES', 'JUDGE', 'KNOWN', 'LABEL', 'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEASE', 'LEAST', 'LEAVE', 'LEGAL', 'LEVEL', 'LEWIS', 'LIGHT', 'LIMIT', 'LINKS', 'LIVES', 'LOCAL', 'LOGIC', 'LOOSE', 'LOWER', 'LUCKY', 'LUNCH', 'LYING', 'MAGIC', 'MAJOR', 'MAKER', 'MARCH', 'MARIA', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT', 'MEDIA', 'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MOTOR', 'MOUNT', 'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC', 'NEEDS', 'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED', 'NOVEL', 'NURSE', 'OCCUR', 'OCEAN', 'OFFER', 'OFTEN', 'ORDER', 'OTHER', 'OUGHT', 'PAINT', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PHOTO', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLAIN', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIME', 'PRINT', 'PRIOR', 'PRIZE', 'PROOF', 'PROUD', 'PROVE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH', 'READY', 'REFER', 'RIGHT', 'RIVAL', 'RIVER', 'ROBIN', 'ROGER', 'ROMAN', 'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SERVE', 'SEVEN', 'SHALL', 'SHAPE', 'SHARE', 'SHARP', 'SHEET', 'SHELF', 'SHELL', 'SHIFT', 'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED', 'SKILL', 'SLEEP', 'SLIDE', 'SMALL', 'SMART', 'SMILE', 'SMITH', 'SMOKE', 'SOLID', 'SOLVE', 'SORRY', 'SOUND', 'SOUTH', 'SPACE', 'SPARE', 'SPEAK', 'SPEED', 'SPEND', 'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAFF', 'STAGE', 'STAKE', 'STAND', 'START', 'STATE', 'STEAM', 'STEEL', 'STICK', 'STILL', 'STOCK', 'STONE', 'STOOD', 'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'SUITE', 'SUPER', 'SWEET', 'TABLE', 'TAKEN', 'TASTE', 'TAXES', 'TEACH', 'TEETH', 'TERRY', 'TEXAS', 'THANK', 'THEFT', 'THEIR', 'THEME', 'THERE', 'THESE', 'THICK', 'THING', 'THINK', 'THIRD', 'THOSE', 'THREE', 'THREW', 'THROW', 'TIGHT', 'TIMES', 'TIRED', 'TITLE', 'TODAY', 'TOPIC', 'TOTAL', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY', 'TRUST', 'TRUTH', 'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL', 'UPPER', 'UPSET', 'URBAN', 'USAGE', 'USUAL', 'VALID', 'VALUE', 'VIDEO', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHEEL', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG', 'WROTE', 'YIELD', 'YOUNG', 'YOUTH', 'ABLE', 'ABOUT', 'ACCOUNT', 'ACID', 'ACROSS', 'ACT', 'ADDITION', 'ADJUSTMENT', 'ADVERTISEMENT', 'AFTER', 'AGAIN', 'AGAINST', 'AGREEMENT', 'AIR', 'ALL', 'ALMOST', 'AMONG', 'AMOUNT', 'AMUSEMENT', 'AND', 'ANGLE', 'ANGRY', 'ANIMAL', 'ANSWER', 'ANT', 'ANY', 'APPARATUS', 'APPLE', 'APPROVAL', 'ARCH', 'ARGUMENT', 'ARM', 'ARMY', 'ART', 'AS', 'AT', 'ATTACK', 'ATTEMPT', 'ATTENTION', 'ATTRACTION', 'AUTHORITY', 'AUTOMATIC', 'AWAKE', 'BABY', 'BACK', 'BAD', 'BAG', 'BALANCE', 'BALL', 'BAND', 'BASE', 'BASIN', 'BASKET', 'BATH', 'BE', 'BEAUTIFUL', 'BECAUSE', 'BED', 'BEE', 'BEFORE', 'BEHAVIOUR', 'BELIEF', 'BELL', 'BENT', 'BERRY', 'BETWEEN', 'BIRD', 'BIRTH', 'BIT', 'BITE', 'BITTER', 'BLACK', 'BLADE', 'BLOOD', 'BLOW', 'BLUE', 'BOARD', 'BOAT', 'BODY', 'BOILING', 'BONE', 'BOOK', 'BOOT', 'BOTTLE', 'BOX', 'BOY', 'BRAIN', 'BRAKE', 'BRANCH', 'BRASS', 'BREAD', 'BREATH', 'BRICK', 'BRIDGE', 'BRIGHT', 'BROKEN', 'BROTHER', 'BROWN', 'BRUSH', 'BUCKET', 'BUILDING', 'BULB', 'BURN', 'BURST', 'BUSINESS', 'BUT', 'BUTTER', 'BUTTON', 'BY', 'CAKE', 'CAMERA', 'CANVAS', 'CARD', 'CARE', 'CARRIAGE', 'CART', 'CAT', 'CAUSE', 'CERTAIN', 'CHAIN', 'CHALK', 'CHANCE', 'CHANGE', 'CHEAP', 'CHEESE', 'CHEMICAL', 'CHEST', 'CHIEF', 'CHIN', 'CHURCH', 'CIRCLE', 'CLEAR', 'CLOCK', 'CLOTH', 'CLOUD', 'COAL', 'COAT', 'COLD', 'COLLAR', 'COLOUR', 'COMB', 'COME', 'COMFORT', 'COMMITTEE', 'COMMON', 'COMPANY', 'COMPARISON', 'COMPETITION', 'COMPLETE', 'COMPLEX', 'CONDITION', 'CONNECTION', 'CONSCIOUS', 'CONTROL', 'COOK', 'COPPER', 'COPY', 'CORD', 'CORK', 'COTTON', 'COUGH', 'COUNTRY', 'COVER', 'COW', 'CRACK', 'CREDIT', 'CRIME', 'CRUEL', 'CRUSH', 'CRY', 'CUP', 'CUP', 'CURRENT', 'CURTAIN', 'CURVE', 'CUSHION', 'DAMAGE', 'DANGER', 'DARK', 'DAUGHTER', 'DAY', 'DEAD', 'DEAR', 'DEATH', 'DEBT', 'DECISION', 'DEEP', 'DEGREE', 'DELICATE', 'DEPENDENT', 'DESIGN', 'DESIRE', 'DESTRUCTION', 'DETAIL', 'DEVELOPMENT', 'DIFFERENT', 'DIGESTION', 'DIRECTION', 'DIRTY', 'DISCOVERY', 'DISCUSSION', 'DISEASE', 'DISGUST', 'DISTANCE', 'DISTRIBUTION', 'DIVISION', 'DO', 'DOG', 'DOOR', 'DOUBT', 'DOWN', 'DRAIN', 'DRAWER', 'DRESS', 'DRINK', 'DRIVING', 'DROP', 'DRY', 'DUST', 'EAR', 'EARLY', 'EARTH', 'EAST', 'EDGE', 'EDUCATION', 'EFFECT', 'EGG', 'ELASTIC', 'ELECTRIC', 'END', 'ENGINE', 'ENOUGH', 'EQUAL', 'ERROR', 'EVEN', 'EVENT', 'EVER', 'EVERY', 'EXAMPLE', 'EXCHANGE', 'EXISTENCE', 'EXPANSION', 'EXPERIENCE', 'EXPERT', 'EYE', 'FACE', 'FACT', 'FALL', 'FALSE', 'FAMILY', 'FAR', 'FARM', 'FAT', 'FATHER', 'FEAR', 'FEATHER', 'FEEBLE', 'FEELING', 'FEMALE', 'FERTILE', 'FICTION', 'FIELD', 'FIGHT', 'FINGER', 'FIRE', 'FIRST', 'FISH', 'FIXED', 'FLAG', 'FLAME', 'FLAT', 'FLIGHT', 'FLOOR', 'FLOWER', 'FLY', 'FOLD', 'FOOD', 'FOOLISH', 'FOOT', 'FOR', 'FORCE', 'FORK', 'FORM', 'FORWARD', 'FOWL', 'FRAME', 'FREE', 'FREQUENT', 'FRIEND', 'FROM', 'FRONT', 'FRUIT', 'FULL', 'FUTURE', 'GARDEN', 'GENERAL', 'GET', 'GIRL', 'GIVE', 'GLASS', 'GLOVE', 'GO', 'GOAT', 'GOLD', 'GOOD', 'GOVERNMENT', 'GRAIN', 'GRASS', 'GREAT', 'GREEN', 'GREY', 'GRIP', 'GROUP', 'GROWTH', 'GUIDE', 'GUN', 'HAIR', 'HAMMER', 'HANGING', 'HAPPY', 'HARBOUR', 'HARD', 'HARMONY', 'HAT', 'HATE', 'HAVE', 'HE', 'HEAD', 'HEALTHY', 'HEAR', 'HEARING', 'HEART', 'HEAT', 'HELP', 'HIGH', 'HISTORY', 'HOLE', 'HOLLOW', 'HOOK', 'HOPE', 'HORN', 'HORSE', 'HOSPITAL', 'HOUR', 'HOUSE', 'HOW', 'HUMOUR', 'I', 'ICE', 'IDEA', 'IF', 'ILL', 'IMPORTANT', 'IMPULSE', 'IN', 'INCREASE', 'INDUSTRY', 'INK', 'INSECT', 'INSTRUMENT', 'INSURANCE', 'INTEREST', 'INVENTION', 'IRON', 'ISLAND', 'JELLY', 'JEWEL', 'JOIN', 'JOURNEY', 'JUDGE', 'JUMP', 'KEEP', 'KETTLE', 'KEY', 'KICK', 'KIND', 'KISS', 'KNEE', 'KNIFE', 'KNOT', 'KNOWLEDGE', 'LAND', 'LANGUAGE', 'LAST', 'LATE', 'LAUGH', 'LAW', 'LEAD', 'LEAF', 'LEARNING', 'LEATHER', 'LEFT', 'LEG', 'LET', 'LETTER', 'LEVEL', 'LIBRARY', 'LIFT', 'LIGHT', 'LIKE', 'LIMIT', 'LINE', 'LINEN', 'LIQUID', 'LIST', 'LITTLE', 'LIVING', 'LOCK', 'LONG', 'LOOK', 'LOOSE', 'LOSS', 'LOUD', 'LOVE', 'LOW', 'MACHINE', 'MAKE', 'MALE', 'MAN', 'MANAGER', 'MAP', 'MARK', 'MARKET', 'MARRIED', 'MASS', 'MATCH', 'MATERIAL', 'MAY', 'MEAL', 'MEASURE', 'MEAT', 'MEDICAL', 'MEETING', 'MEMORY', 'METAL', 'MIDDLE', 'MILITARY', 'MILK', 'MIND', 'MINE', 'MINUTE', 'MIST', 'MIXED', 'MONEY', 'MONKEY', 'MONTH', 'MOON', 'MORNING', 'MOTHER', 'MOTION', 'MOUNTAIN', 'MOUTH', 'MOVE', 'MUCH', 'MUSCLE', 'MUSIC', 'NAIL', 'NAME', 'NARROW', 'NATION', 'NATURAL', 'NEAR', 'NECESSARY', 'NECK', 'NEED', 'NEEDLE', 'NERVE', 'NET', 'NEW', 'NEWS', 'NIGHT', 'NO', 'NOISE', 'NORMAL', 'NORTH', 'NOSE', 'NOT', 'NOTE', 'NOW', 'NUMBER', 'NUT', 'OBSERVATION', 'OF', 'OFF', 'OFFER', 'OFFICE', 'OIL', 'OLD', 'ON', 'ONLY', 'OPEN', 'OPERATION', 'OPINION', 'OPPOSITE', 'OR', 'ORANGE', 'ORDER', 'ORGANIZATION', 'ORNAMENT', 'OTHER', 'OUT', 'OVEN', 'OVER', 'OWNER', 'PAGE', 'PAIN', 'PAINT', 'PAPER', 'PARALLEL', 'PARCEL', 'PART', 'PAST', 'PASTE', 'PAYMENT', 'PEACE', 'PEN', 'PENCIL', 'PERSON', 'PHYSICAL', 'PICTURE', 'PIG', 'PIN', 'PIPE', 'PLACE', 'PLANE', 'PLANT', 'PLATE', 'PLAY', 'PLEASE', 'PLEASURE', 'PLOUGH', 'POCKET', 'POINT', 'POISON', 'POLISH', 'POLITICAL', 'POOR', 'PORTER', 'POSITION', 'POSSIBLE', 'POT', 'POTATO', 'POWDER', 'POWER', 'PRESENT', 'PRICE', 'PRINT', 'PRISON', 'PRIVATE', 'PROBABLE', 'PROCESS', 'PRODUCE', 'PROFIT', 'PROPERTY', 'PROSE', 'PROTEST', 'PUBLIC', 'PULL', 'PUMP', 'PUNISHMENT', 'PURPOSE', 'PUSH', 'PUT', 'QUALITY', 'QUESTION', 'QUICK', 'QUIET', 'QUITE', 'RAIL', 'RAIN', 'RANGE', 'RAT', 'RATE', 'RAY', 'REACTION', 'READING', 'READY', 'REASON', 'RECEIPT', 'RECORD', 'RED', 'REGRET', 'REGULAR', 'RELATION', 'RELIGION', 'REPRESENTATIVE', 'RESPECT', 'RESPONSIBLE', 'REST', 'REWARD', 'RHYTHM', 'RICE', 'RIGHT', 'RING', 'RIVER', 'ROAD', 'ROD', 'ROLL', 'ROOF', 'ROOM', 'ROOT', 'ROUGH', 'ROUND', 'RUB', 'RULE', 'RUN', 'SAD', 'SAFE', 'SAIL', 'SALT', 'SAME', 'SAND', 'SAY', 'SCALE', 'SCHOOL', 'SCIENCE', 'SCISSORS', 'SCREW', 'SEA', 'SEAT', 'SECOND', 'SECRET', 'SECRETARY', 'SEE', 'SEED', 'SEEM', 'SELECTION', 'SELF', 'SEND', 'SENSE', 'SEPARATE', 'SERIOUS', 'SERVANT', 'SEX', 'SHADE', 'SHAKE', 'SHAME', 'SHARP', 'SHEEP', 'SHELF', 'SHIP', 'SHIRT', 'SHOCK', 'SHOE', 'SHORT', 'SHUT', 'SIDE', 'SIGN', 'SILK', 'SILVER', 'SIMPLE', 'SISTER', 'SIZE', 'SKIN', '', 'SKIRT', 'SKY', 'SLEEP', 'SLIP', 'SLOPE', 'SLOW', 'SMALL', 'SMASH', 'SMELL', 'SMILE', 'SMOKE', 'SMOOTH', 'SNAKE', 'SNEEZE', 'SNOW', 'SO', 'SOAP', 'SOCIETY', 'SOCK', 'SOFT', 'SOLID', 'SOME', '', 'SON', 'SONG', 'SORT', 'SOUND', 'SOUP', 'SOUTH', 'SPACE', 'SPADE', 'SPECIAL', 'SPONGE', 'SPOON', 'SPRING', 'SQUARE', 'STAGE', 'STAMP', 'STAR', 'START', 'STATEMENT', 'STATION', 'STEAM', 'STEEL', 'STEM', 'STEP', 'STICK', 'STICKY', 'STIFF', 'STILL', 'STITCH', 'STOMACH', 'STONE', 'STOP', 'STORE', 'STORY', 'STRAIGHT', 'STRANGE', 'STREET', 'STRETCH', 'STRONG', 'STRUCTURE', 'SUBSTANCE', 'SUCH', 'SUDDEN', 'SUGAR', 'SUGGESTION', 'SUMMER', 'SUN', 'SUPPORT', 'SURPRISE', 'SWEET', 'SWIM', 'SYSTEM', 'TABLE', 'TAIL', 'TAKE', 'TALK', 'TALL', 'TASTE', 'TAX', 'TEACHING', 'TENDENCY', 'TEST', 'THAN', 'THAT', 'THE', 'THEN', 'THEORY', 'THERE', 'THICK', 'THIN', 'THING', 'THIS', 'THOUGHT', 'THREAD', 'THROAT', 'THROUGH', 'THROUGH', 'THUMB', 'THUNDER', 'TICKET', 'TIGHT', 'TILL', 'TIME', 'TIN', 'TIRED', 'TO', 'TOE', 'TOGETHER', 'TOMORROW', 'TONGUE', 'TOOTH', 'TOP', 'TOUCH', 'TOWN', 'TRADE', 'TRAIN', 'TRANSPORT', 'TRAY', 'TREE', 'TRICK', 'TROUBLE', 'TROUSERS', 'TRUE', 'TURN', 'TWIST', 'UMBRELLA', 'UNDER', 'UNIT', 'UP', 'USE', 'VALUE', 'VERSE', 'VERY', 'VESSEL', 'VIEW', 'VIOLENT', 'VOICE', 'WAITING', 'WALK', 'WALL', 'WAR', 'WARM', 'WASH', 'WASTE', 'WATCH', 'WATER', 'WAVE', 'WAX', 'WAY', 'WEATHER', 'WEEK', 'WEIGHT', 'WELL', 'WEST', 'WET', 'WHEEL', 'WHEN', 'WHERE', 'WHILE', 'WHIP', 'WHISTLE', 'WHITE', 'WHO', 'WHY', 'WIDE', 'WILL', 'WIND', 'WINDOW', 'WINE', 'WING', 'WINTER', 'WIRE', 'WISE', 'WITH', 'WOMAN', 'WOOD', 'WOOL', 'WORD', 'WORK', 'WORM', 'WOUND', 'WRITING', 'WRONG', 'YEAR', 'YELLOW', 'YES', 'YESTERDAY', 'YOU', 'YOUNG', 'BREYTENBACH', 'ANDROID']
    return random.choice(lis).lower()

def print_board(board,guess_history):
    hangman_drawings = [
    """
    -----
    |   |
    |   0
    |  / \ 
    |   | 
    |  / \ 
    |
    --------
    """,
    """
    -----
    |   |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  /  
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  / \ 
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  / \ 
    |   | 
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  / \ 
    |   | 
    |  /  
    |
    --------
    """]
    print(hangman_drawings[-remaining_guesses],end='')
    st = '  '
    for i in board:
        st = st+i+' '
    print(st)
    print(f'Guess History: {guess_history}')
#PROJECT 3 HANGMAN
#AUTHOR: Ben Martino
#------------------------------------
#YOUR PROGRAM STARTS HERE:
def update_board(c,board):
    for i in range(len(secret_word)):
        if secret_word[i] == c:
            board[i] = c
        else:
            continue

remaining_guesses = 6
guess_history = []
secret_word = get_random_word()
board = ['_']*len(secret_word)
correct_guesses = []

while remaining_guesses>0:
    print_board(board,guess_history)
    c = input("Guess Letter: ")
    if c in guess_history or len(c) != 1 or c not in 'abcdefghijklmnopqrstuvwxyz': #Extra Credit 1
        print("Invalid guess") 
    else:
        guess_history.append(c)
        guess_history.sort() # Extra Credit 3
        if c in secret_word:
            print(f"Good guess, you have {remaining_guesses} guesses left")
            update_board(c,board)
            correct_guesses.append(c)
        else:
            remaining_guesses = remaining_guesses -1
            print(f"{c} not in word. You have {remaining_guesses} guesses left")    
    if len(correct_guesses) == len(secret_word):
        break
    else:
        continue
    
print_board(board,guess_history)
if remaining_guesses == 0:
    print(f"You've LOST, the word was {secret_word}")  
else: 
    print(f"You've WON, the word was {secret_word}")
#------------------------------------