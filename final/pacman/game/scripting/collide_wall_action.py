from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point


class CollideWallAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        walls = cast.get_actors(WALL_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        pacman = cast.get_first_actor(PACMAN_GROUP)
        pacman_body = pacman.get_body()
        
        
        for wall in walls:
            wall_body = wall.get_body()
            pacman_position = pacman_body.get_position()

            if self._physics_service.is_above(pacman_body, wall_body):
                pacman.stop_moving()
                pacman_body.set_position(Point(pacman_position.get_x(), pacman_position.get_y() - PACMAN_VELOCITY))

            if self._physics_service.is_below(pacman_body, wall_body):
                pacman.stop_moving()
                pacman_body.set_position(Point(pacman_position.get_x(), pacman_position.get_y() + PACMAN_VELOCITY))

            if self._physics_service.is_left_of(pacman_body, wall_body):
                pacman.stop_moving()
                pacman_body.set_position(Point(pacman_position.get_x() - PACMAN_VELOCITY, pacman_position.get_y()))     

            if self._physics_service.is_right_of(pacman_body, wall_body):
                pacman.stop_moving()
                pacman_body.set_position(Point(pacman_position.get_x() + PACMAN_VELOCITY, pacman_position.get_y()))           
        
