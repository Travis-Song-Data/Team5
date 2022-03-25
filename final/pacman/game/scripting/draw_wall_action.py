from constants import *
from game.scripting.action import Action


class DrawWallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        walls = cast.get_actors(WALL_GROUP)
        
        for wall in walls:
            body = wall.get_body()

            if wall.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            self._video_service.draw_rectangle(rectangle, RED)