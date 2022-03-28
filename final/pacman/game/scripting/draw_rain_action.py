from constants import *
from game.scripting.action import Action
import random
from game.casting.point import Point

class DrawRainAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        rains = cast.get_actors(RAIN_GROUP)
        for rain in rains:

            image = rain.get_image()
            x = random.randint(1, SCREEN_WIDTH - 1)
            y = random.randint(1, SCREEN_HEIGHT - 1)
            position = Point(x, y)
            self._video_service.draw_image(image, position)