from puzzle import puzzle
from output_service import output_service

class director:
    def __init__(self):
        self.correct_guesses = []
    
    def play_games(self):
        # Get a puzzle word
        puzzle_word = puzzle.get_puzzle_word()
        # Create a list of booleans, the same number as there are letters
        # in the puzzle word
        
        for num in range(len(puzzle_word)):
            self.correct_guesses.append(False)
        # Create list of incorrect guesses (list of strings)


        word_is_guessed = False
        jumper_alive = True
        while (not word_is_guessed or not jumper_alive): # Continue until they guess the word or the jumper loses
            # Display proper number of underscores
            output_service.display_word(puzzle_word, self.add_correct_guesses(puzzle.correct_guess(puzzle_word,letter_guessed)))
            # Display the jumper
            output_service.display_jumper()
            # Prompt for a guess
            letter_guessed = input("Please choose a letter: ")
    
    def add_correct_guesses(self, correct_indices):
        for i in correct_indices:
            self.correct_guesses[i] = True


play = director()
play.play_games()