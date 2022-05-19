from game.word_bank import Words
from game.letter_checker import Letters


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        Words: A list of word.
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Ask the user to guess a letter from a - z.

        Args:
            self (Director): An instance of Director.
        """
        self.guess = input('Guess a letter [a-z]: ')
        
    def _do_updates(self):
        # line cut
        pass

    def _do_outputs(self):
        """Check if the puzzle is solved.

        Args:
            self (Director): An instance of Director.
        """
        if the puzzle is solve, the game is over. # condition: how to determine puzzle is solved? when all letter guess correctly.
        print('Puzzle solved.')
        if the player has no more parachute, the game is over. # condition: how to determine the game is over? when all the line is cut.
        print('No more parachute. Game over.')
    




    