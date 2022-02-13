'''Parachute class
   Draw the parachute and remove one line when player's guessing is incorrect.
   
   self._drawing_list: The structure of the parachute
   self._turn: Count how many time had the player guessed incorrect. When count ups to 4, the little man die. Game over'''
class Parachute:
    ''''''
    def __init__(self):

        self._drawing_list = [' ___', 
                              '/___\\', 
                              '\   /',
                              ' \ /', 
                              '  o', 
                              ' /|\\', 
                              ' / \\']
        self._turn = 0

    def drawing(self):
        '''Drawing and print the parachute'''
        for i in self._drawing_list:
            print(i)


    def remove(self, answer):
        '''Require an "answer" parameter which is a boolean parameter.
           If answer is Ture, meaning that player guessed the right letter, so nothing will happen.
           If answer is Flase, meaning that player guessed wrong, the parachute will be cut one line.'''
        if answer == False:
            self._turn += 1
            if self._turn <= 3:
                self._drawing_list.pop(0)
            elif self._turn == 4:
                self._drawing_list.pop(0)
                self._drawing_list[0] = '  x'
        else:
            return