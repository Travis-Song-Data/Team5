from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class DrawBackgroundAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        background = cast.get_first_actor(BACKGROUND_GROUP)
            
        image = background.get_image()
        position = Point(BACKGROUND_X, BACKGROUND_Y)
        self._video_service.draw_image(image, position)