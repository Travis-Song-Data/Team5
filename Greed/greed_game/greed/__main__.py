import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
SCOREE_SIZE = 25
COLS = 60
ROWS = 40
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 100


def main():
    
    # create the cast
    cast = Cast()

    score = Actor()
    score.set_text("Point: ")
    points = score.get_text()
    score.set_font_size(SCOREE_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(SCOREE_SIZE, 0))
    cast.add_actor("scores", score)

    
    # create the robot
    x = int(MAX_X / 2)
    y = MAX_Y - 15
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts


    for n in range(DEFAULT_ARTIFACTS):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        rocks = Artifact()
        velocity1 = Point(0, 3)
        rocks.set_velocity(velocity1)
        rocks.set_font_size(CELL_SIZE)
        rocks.set_color(color)
        rocks.set_position(position)
        cast.add_actor("rocks", rocks)
    
    for n in range(DEFAULT_ARTIFACTS):

        x = random.randint(1, COLS - 1)
        y = y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gems = Artifact()
        velocity2 = Point(0, 5)
        gems.set_velocity(velocity2)
        gems.set_text("$")
        gems.set_font_size(FONT_SIZE)
        gems.set_color(color)
        gems.set_position(position)
        cast.add_actor("gems", gems)


    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast, points)


if __name__ == "__main__":
    main()