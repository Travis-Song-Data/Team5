from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.scripting.play_sound_action import PlaySoundAction

class CollideFoodAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
          
    def execute(self, cast, script, callback):
        foods = cast.get_actors(FOOD_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        pacman = cast.get_first_actor(PACMAN_GROUP)

        for food in foods:
            food_body = food.get_body()
            pacman_body = pacman.get_body()
            if self._physics_service.has_collided(pacman_body, food_body):
                sound = Sound(EAT_FOOD_SOUND)
                self._audio_service.play_sound(sound)
                points = food.get_points()
                stats.add_points(points)
                cast.remove_actor(FOOD_GROUP, food)