from constants import *
from game.casting.actor import Actor

class Ghost(Actor):

    def __init__(self, body, animation, debug=False):
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_body(self):

        return self._body

    def get_animation(self):

        return self._animation