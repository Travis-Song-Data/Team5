from puzzle import puzzle
from parachute import Parachute


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
        self.word = puzzle()


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


def word_list(self, puzzle_word, letter):
    """Gets the chosen list from the puzzle class"""
    indices = []
    length_of_puzzle = len(puzzle_word) - 1

    for i in length_of_puzzle:
        if letter == puzzle_word[i]:
            indices.append(i)

        return indices



    #random_word = self.word.callword()
    #  for i in len(random_word)
    #   print('-')
    # if self.guess_letter in random_word:
    # find indices of the word and replace in that position
    # replace the word with the correct guessed letter
    # else:
    # store in the list of words that was guessed wrong

    #
    # return random_word


jumper = Parachute()
for i in range(5):  # Where game starts
    jumper.drawing()
    jumper.remove(False)  # or Ture
