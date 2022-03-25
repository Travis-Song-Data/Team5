from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        pacman = cast.get_first_actor(PACMAN_GROUP)
        
        for brick in bricks:
            brick_body = brick.get_body()
            pacman_body = pacman.get_body()
            pacman_position = pacman_body.get_position()

            # if self._physics_service.has_collided(pacman_body, brick_body):
            #     # sound = Sound(BOUNCE_SOUND)
            #     # self._audio_service.play_sound(sound)
            #     # points = brick.get_points()
            #     # stats.add_points(points)
            #     # cast.remove_actor(BRICK_GROUP, brick)
            #     pacman.stop_moving()
            #     pacman_body.set_position(Point(pacman_position.get_x()-10, pacman_position.get_y()-10))

            if self._physics_service.is_above(pacman_body, brick_body):
                pacman.stop_moving()
                pacman_body.set_position(Point(pacman_position.get_x(), pacman_position.get_y() - PACMAN_VELOCITY))

            if self._physics_service.is_below(pacman_body, brick_body):
                pacman.stop_moving()
                pacman_body.set_position(Point(pacman_position.get_x(), pacman_position.get_y() + PACMAN_VELOCITY))

            if self._physics_service.is_left_of(pacman_body, brick_body):
                pacman.stop_moving()
                pacman_body.set_position(Point(pacman_position.get_x() - PACMAN_VELOCITY, pacman_position.get_y()))     

            if self._physics_service.is_right_of(pacman_body, brick_body):
                pacman.stop_moving()
                pacman_body.set_position(Point(pacman_position.get_x() + PACMAN_VELOCITY, pacman_position.get_y()))           
        
