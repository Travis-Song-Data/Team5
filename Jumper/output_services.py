

class output_service:

    #instantiated generator
    def __init__(self ):

        pass

    def display_word(self, word, letters_that_are_correct, display_word):

        
        for i in range(len(word)):
            if word[i] in letters_that_are_correct:
                display_word[i] = word[i]


        tmp = ""
        for c in display_word:
            tmp += c + ' '
        print(tmp)

        

    


    


        
