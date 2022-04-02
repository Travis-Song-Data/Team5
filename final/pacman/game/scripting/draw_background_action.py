from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class DrawBackgroundAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        backgrounds = cast.get_actors(BACKGROUND_GROUP)
        for background in backgrounds:
            
            image = background.get_image()
            position = Point(BACKGROUND_X, BACKGROUND_Y)
            self._video_service.draw_image(image, position)