from game.casting.actor import Actor


class Wall(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, image, debug = False):
        """Constructs a new Wall.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        

    def get_body(self):
        """Gets the wall's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image