from game.casting.actor import Actor

class Food(Actor):

    def __init__(self, body, image, point, debug = False):
        super().__init__(debug)
        self._body = body
        self._image = image
        self._point = point
    def get_body(self):
        return self._body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image


    def get_points(self):
        """Gets the wall's points.
        
        Returns:
            A number representing the wall's points.
        """
        return self._point