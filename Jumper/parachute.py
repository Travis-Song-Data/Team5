class Parachute:

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
        for i in self._drawing_list:
            print(i)


    def remove(self, answer):
        if answer == False:
            self._turn += 1
            if self._turn <= 3:
                self._drawing_list.pop(0)
            elif self._turn == 4:
                self._drawing_list.pop(0)
                self._drawing_list[0] = '  x'