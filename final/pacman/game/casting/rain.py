from game.casting.actor import Actor


# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Rain(Actor):

    def __init__(self, image, body):
        super().__init__()
        self._image = image
        self._body = body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):

        return self._body