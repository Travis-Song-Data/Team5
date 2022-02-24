class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._scores = 0
        
    def start_game(self, cast, scores):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            scores : The scores.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast, scores)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast, points):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        score = cast.get_first_actor("scores")
        robot = cast.get_first_actor("robots")
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")

        score.set_text(f"{points} {self._scores}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        for rock in rocks:
            rock.move_next(max_x, max_y)
            if robot.get_position().equals(rock.get_position()):
                self._scores -= 50
        
        for gem in gems:
            gem.move_next(max_x, max_y)
            if robot.get_position().equals(gem.get_position()):
                self._scores += 50
        
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")
        score = cast.get_first_actor("scores")
        robot = cast.get_first_actor("robots")
        self._video_service.draw_rocks(rocks)
        self._video_service.draw_gems(gems)
        self._video_service.draw_robot(robot)
        self._video_service.draw_score(score)
        self._video_service.flush_buffer()
