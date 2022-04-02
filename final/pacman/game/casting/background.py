from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Background(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, image, body):
        """Constructs a new Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__()
        self._image = image
        self._body =body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    
    def get_body(self):

        return self._body