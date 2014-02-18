"""
This file contains various constants to be used in the program. (Read: constants, so
don't go changing them in the code). Some of these could likely be pulled out of here
and added as member variables to the various classes instead. (Like MAX_VOTES,
especially since you may want to set that programmatically).

"""


# Maps the aciton name (that we get in chat) to the key to be sent to AutoHotKey
ALL_TYPES = { 'FORWARD': 'w', 'BACK': 's', 'LEFT': 'a',
               'RIGHT': 'd', 'RUN': 'RUN', 'ROLL': 'ROLL', 'SHIELD': 'm',
               'R1': 'h', 'R2': 'u', 'ESTUS': 'e', 'INTERACT': 'q',
               'ENTER': 'ENTER', 'CENTERCAM': 'o'}

# Just an enumeration of sorts on these
ACTION = 0
MOVEMENT = 1
START = 13 

# Whether or not in testing; 
TESTING = True

# Put your IRC details in the following fields
BOT_OWNER = 'username' # Your username (not 100% necessary)
NICK = 'botusername' # Your bot's username
CHANNEL = '#channel' # The channel you want to connect to
SERVER = 'irc.twitch.tv' # Leave this
PORT = 6667 # Leave this
AUTH = 'token' # Your Twitch auth token

# The amount of time actions and movements should execute. So, for example,
# you will move "FORWARD" for whatever you set MOVEMENT_TIME to. This is just the default,
# and you can set it to whatever you want when creating an Action object.
ACTION_TIME = 1
MOVEMENT_TIME = .5

ACTIONS = ['R1','R2','ESTUS','INTERACT','ENTER','CENTERCAM']
MOVEMENTS = ['FORWARD','BACK','LEFT','RIGHT','RUN','SHIELD', 'ROLL']

MAX_VOTES = 10

if TESTING:
    MAX_VOTES = 1