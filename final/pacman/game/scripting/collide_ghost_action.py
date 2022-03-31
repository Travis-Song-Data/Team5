from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.scripting.play_sound_action import PlaySoundAction

class CollideGhostAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
          
    def execute(self, cast, script, callback):
        ghosts = cast.get_actors(GHOST_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        pacman = cast.get_first_actor(PACMAN_GROUP)

        for ghost in ghosts:
            ghost_body = ghost.get_body()
            pacman_body = pacman.get_body()
            if self._physics_service.has_collided(pacman_body, ghost_body):
                sound = Sound(OVER_SOUND)
                self._audio_service.play_sound(sound)
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
                
                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN) 
                else:
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(sound)

