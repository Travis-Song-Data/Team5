import random

class Card:
    '''Cards from 1 to 13.

    The responsibility of Card is to draw two cards from the desk.

    Attributes:
        drawn_card(int): draw a card from 1 to 13.
    '''
    def __init__(self):
        '''Constructs a new instance of Card.

        Args:
            self(Card): An instance of Card.
        '''
        self.drawn_card = 0

    def draw_card(self):
        '''Draw a card.

        Args:
            self(Card): An instance of Card.
        '''
        self.drawn_card = random.randint(1, 13)
        return self.drawn_card
    

    def display_card(self, A, card):
        '''Display the card player drew.
        
        Args:
            self(Card): An instance of Card.
        '''
        print(A, 'card is', card)
