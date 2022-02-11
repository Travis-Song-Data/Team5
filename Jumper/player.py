#import puzzle

class Player:
    """ The responsibility of the player class is to ask for a letter from the user, store the letter.
    The player will guess the letter to put in.
    """

    def __init__(self):
        """constructs a new Player

        Args:
            self (player): An instance of player.
        """
        self.is_playing = True
        # self.word = puzzle()


def start_game(self):
    """Starts the game by running the main game loop.

    Args:
        self (player): an instance of Director.
        """
    while self.is_playing:
        self.user_input()
        self.word_list()


def user_input(self):
    """Gets a letter from the user

    Returns: the input from user"""
    input_letter = input("Guess a letter [a-z]: ")
    return input_letter


def word_list(self):
    """Gets the chosen list from the puzzle class"""
    #random_word = self.word.callword()
    # return random_word
    pass
