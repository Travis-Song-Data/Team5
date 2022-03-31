from constants import *
from game.casting.point import Point
from game.scripting.action import Action

class MoveGhostAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        body = pacman.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()