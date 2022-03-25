from constants import *
from game.casting.actor import Actor


class Wall(Actor):

    def __init__(self, body, debug=False):
        super().__init__(debug)
        self._body = body

    def get_body(self):

        return self._body