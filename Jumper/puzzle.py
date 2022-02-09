import random

class puzzle:

    def __init__(self):
        self.word_list = ['about','actor','above','acute','admit','adopt','adult','after','again','agent','agree','ahead','alarm','album','alive']
        

    def call_word(self):
        word = random.choice(self.word_list)

        return word
