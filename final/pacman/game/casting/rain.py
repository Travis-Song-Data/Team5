from game.casting.actor import Actor


# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Rain(Actor):

    def __init__(self, image, velocity):
        super().__init__()
        self._image = image
        self._velocity = velocity

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_velocity(self):
        """Gets the body's velocity.
        
        Returns:
            An instance of Point containing the horizontal and vertical speed.
        """
        return self._velocity