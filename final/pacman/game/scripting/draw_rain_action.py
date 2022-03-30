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
            body = rain.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            new_position = position.add(velocity)
            body.set_position(new_position)
            y = new_position.get_y()
            x = new_position.get_x()
            if y >= FIELD_BOTTOM:
                new_position = Point(x, FIELD_TOP)
                body.set_position(new_position)
            image = rain.get_image()
            self._video_service.draw_image(image, new_position)
            

