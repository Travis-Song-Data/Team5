from jumper import jumper

class output_service:
    
    def display_word(self, puzzle_word, correct_guesses):
        num_letters = len(puzzle_word) - 1
        for i in range(0, num_letters):
            if correct_guesses[i] == True:
                print(puzzle_word[i])
            else:
                print("_")


    def display_jumper(self):
        print(jumper.check_parachute())

