from card import Card

class Player:
    """A person who play the game. 
    
    The responsibility of a Player is to control the sequence of play.

    Attributes:
        keep_playing(boolean): Whether or not the game is being played.
        total_scores(int): The scores for the entire game.
        points(int): The points of one round play.
        answer(str): A value to decide the next card is higher than the first card or not
    """
    
    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self.keep_playing = True
        self.total_scores = 400
        self.points = 0
        self.answer = ''


    def start(self):
        """Start the game by runing the main game loop.
        
        Args:
            self (Player): an instance of Player.
        """
        card = Card()
        card.draw_card()
        while self.keep_playing:
            card_one = card.drawn_card 
            card.draw_card()
            card_two = card.drawn_card
            if card_two > card_one:
                self.answer = 'h'
            elif card_two < card_one:
                self.answer = 'l'
            elif card_two == card_one:
                self.answer = ''
            card.display_card('This', card_one)
            self.player_guess()
            card.display_card('Next', card_two)
            self.display_score()
            self.lose_game()
            self.playing_or_not()


    def playing_or_not(self):
        """Start the game by runing the main game loop.
        
        Args:
            self (Player): an instance of Player.
        """
        if not self.keep_playing:
            return
            
        playing_or_not = input('Play again? [y/n]')
        self.keep_playing = (playing_or_not == 'y')

    def player_guess(self):
        '''Ask the player to guess the second card is higher or lower than the first card.
        
        Args:
            self(Scores): An instance of Socres
        '''
        higher_or_lower = input('higher or lower? [h/l]')
        if higher_or_lower == self.answer:
            self.points = 100
        else:
            self.points = -75

    def display_score(self):
        """Display the total socres to player.
        
        Args:
            self (Player): an instance of Player.
        """
        self.total_scores += self.points
        print('You score is', self.total_scores)

    def lose_game(self):
        """Check if the total scores is beyond 0, if it is, then the game is over.
        
        Args:
            self (Player): an instance of Player.
        """
        if self.total_scores <= 0:
            print('You lose, game over.')
            self.keep_playing = False

    