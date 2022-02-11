import random

class puzzle():

    def __init__(self):
        self.word_list = ['about','actor','above','acute','admit','adopt','adult','after','again','agent','agree','ahead','alarm','album','alive']

    def get_puzzle_word(self):
        word_choice = random.choice(self.word_list)

        return word_choice
    
    def correct_guess(self, puzzle_word, letter):
        correct_indices = []

        length_puzzle_word = len(puzzle_word) - 1

        for i in length_puzzle_word:
            if letter == puzzle_word[i]:
                correct_indices.append(i)

        return correct_indices