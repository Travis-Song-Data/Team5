from constants import *
from game.casting.point import Point
from game.scripting.action import Action

class MoveGhostAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        body = pacman.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()

        ghost = cast.get_first_actor(GHOST_GROUP)
        g_body = ghost.get_body()
        position = g_body.get_position()
        g_x = position.get_x()
        g_y = position.get_y()

        if x < g_x:
            if y > g_y:
                if g_x - x >= y - g_y:
                    g_velocity = Point(-GHOST_VELOCITY, 0)
                    new_position = position.add(g_velocity)
                    g_body.set_position(new_position)
                else:
                    g_velocity = Point(0, GHOST_VELOCITY)
                    new_position = position.add(g_velocity)
                    g_body.set_position(new_position)
            if y <= g_y:
                if g_x - x >= g_y - y:
                    g_velocity = Point(-GHOST_VELOCITY, 0)
                    new_position = position.add(g_velocity)
                    g_body.set_position(new_position)
                else:
                    g_velocity = Point(0, -GHOST_VELOCITY)
                    new_position = position.add(g_velocity)
                    g_body.set_position(new_position)

        if x >= g_x:
            if y > g_y:
                if x- g_x >= y - g_y:
                    g_velocity = Point(GHOST_VELOCITY, 0)
                    new_position = position.add(g_velocity)
                    g_body.set_position(new_position)
                else:
                    g_velocity = Point(0, GHOST_VELOCITY)
                    new_position = position.add(g_velocity)
                    g_body.set_position(new_position)
            if y <= g_y:
                if x- g_x >= g_y - y:
                    g_velocity = Point(GHOST_VELOCITY, 0)
                    new_position = position.add(g_velocity)
                    g_body.set_position(new_position)
                else:
                    g_velocity = Point(0, -GHOST_VELOCITY)
                    new_position = position.add(g_velocity)
                    g_body.set_position(new_position)
