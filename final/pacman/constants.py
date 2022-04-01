from raylib import BACKGROUND_COLOR
from game.casting.color import Color
import pathlib


ROOT_PATH = pathlib.Path(__file__).parent.resolve().parent.resolve()
# print(ROOT_PATH)
# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "pacman"
FRAME_RATE = 60

# BACKGROUND
BACKGROUND_GROUP = "background"
BACKGROUND_IMAGE = str(ROOT_PATH.joinpath("pacman/assets/images/120.png"))
BACKGROUND_X = 0
BACKGROUND_Y = -5

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 0
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = str(ROOT_PATH.joinpath("pacman/assets/fonts/zorque.otf"))
print(FONT_FILE)
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BACKGROUND_SOUND = str(ROOT_PATH.joinpath("pacman/assets/sounds/background.wav"))
EAT_FOOD_SOUND = str(ROOT_PATH.joinpath("pacman/assets/sounds/eat.wav"))
WELCOME_SOUND = str(ROOT_PATH.joinpath("pacman/assets/sounds/load.wav"))
OVER_SOUND = str(ROOT_PATH.joinpath("pacman/assets/sounds/scream.wav"))

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
RED = Color(255, 0, 0)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = str(ROOT_PATH.joinpath("pacman/assets/data/level-000.txt"))
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# FOODS
FOOD_GROUP = "foods"
FOOD_IMAGES = str(ROOT_PATH.joinpath("pacman/assets/images/food.png"))
FOOD_WIDTH = 30
FOOD_HEIGHT = 30 
FOOD_FILE = str(ROOT_PATH.joinpath("pacman/assets/data/food_map.txt"))
FOOD_POINT = 5

# RAINS
RAIN_GROUP = "rains"
DEFAULT_RAINS = 100
RAIN_IMAGES = str(ROOT_PATH.joinpath("pacman/assets/images/130.png"))
RAIN_VELOCITY = 7

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"


# PACMAN
PACMAN_GROUP = "pacman"
PACMAN_IMAGES_RIGHT = [str(ROOT_PATH.joinpath(f"pacman/assets/images/{n:03}.png")) for n in range(100, 103)]
PACMAN_IMAGES_LEFT = [str(ROOT_PATH.joinpath(f"pacman/assets/images/{n:03}.png")) for n in range(107, 109)]
PACMAN_IMAGES_UP = [str(ROOT_PATH.joinpath(f"pacman/assets/images/{n:03}.png")) for n in range(104, 106)]
PACMAN_IMAGES_DOWN = [str(ROOT_PATH.joinpath(f"pacman/assets/images/{n:03}.png")) for n in range(110, 112)]
PACMAN_WIDTH = 30
PACMAN_HEIGHT = 30
PACMAN_RATE = 6
PACMAN_VELOCITY = 4

# WALL
WALL_GROUP = "walls"
WALL_IMAGES = str(ROOT_PATH.joinpath(f"pacman/assets/images/010.png"))
WALL_WIDTH = 80
WALL_HEIGHT = 30
WALL_DELAY = 0.5
WALL_RATE = 6
WALL_POINTS = 50

# GHOST
GHOST_GROUP = "ghosts"
GHOST_IMAGES_RIGHT = [str(ROOT_PATH.joinpath(f"pacman/assets/images/{n:03}.png")) for n in range(100, 103)]
GHOST_IMAGES_LEFT = [str(ROOT_PATH.joinpath(f"pacman/assets/images/{n:03}.png")) for n in range(107, 109)]
GHOST_IMAGES_UP = [str(ROOT_PATH.joinpath(f"pacman/assets/images/{n:03}.png")) for n in range(104, 106)]
GHOST_IMAGES_DOWN = [str(ROOT_PATH.joinpath(f"pacman/assets/images/ghost.png"))]
GHOST_WIDTH = 30
GHOST_HEIGHT = 30
GHOST_RATE = 6
GHOST_VELOCITY = 1

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"