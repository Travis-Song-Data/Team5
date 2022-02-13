
from puzzle import puzzle
from parachute import Parachute
from output_services import output_service

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
        self.letters_that_are_correct = []
        self.word = puzzle()
        self.jumper = Parachute()
        self.display_word = []
        
        # self.display = output_service()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (player): an instance of Director.
            """
        word = self.word.call_word()
        self.get_len_of_word(word)
        print(word)
        while self.is_playing:
            letter = self.user_input()
            guess = self.word_list(word, letter)
            self.jumper.remove(guess)
            print(self.letters_that_are_correct)
            self.jumper.drawing()

            # self.display.display_word(word, self.letters_that_are_correct, self.display_word)

            # display_word is the method you are going to create in the output_services class
            # word is the puzzle word you put as a parameter
            # self.letter_that_are_correct is a list that contains all the correct letter player had guessed
            # self.display_word is the initially  _ _ _ _ _. You need to wirte the methoud replace _ to the correct
            # letter in a correct location.
            self.keep_playing(self.jumper)

    def user_input(self):
        """Gets a letter from the user

        Returns: the input from user"""
        input_letter = input("Guess a letter [a-z]: ")
        return input_letter

    def word_list(self, puzzle_word, letter):
        """Gets the chosen list from the puzzle class"""
        length_of_puzzle = len(puzzle_word)
        for i in range(length_of_puzzle):
            if letter == puzzle_word[i]:
                self.letters_that_are_correct.append(letter)
                guess = True
                return
        guess = False
        return guess
    
    def keep_playing(self, parachute):
        """Keep tracking if the game is over"""
        if parachute._drawing_list[0] == '  x':
            self.is_playing = False

        if '_' not in self.display_word:
            self.is_playing = False

    
    def get_len_of_word(self, puzzle_word):
        num_letters = len(puzzle_word)
        for i in range(num_letters):
            self.display_word.append('_')



play = Player()
play.start_game()
