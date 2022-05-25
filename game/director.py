from game.word_bank import Words
from game.letter_checker import Letters
from game.terminal_service import terminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word_bank (Words): A list of words.
        letter_checker (Letters): Check the letter entered by the user.  
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word_bank = Words()
        self._letter_checker = Letters()
        self._terminalService = terminalService()
        self._terminalService.word = self._word_bank.random_word().lower()
        self._terminalService.add_word()
        self._is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()

    def _get_inputs(self):
        """Ask the user to guess a letter.

        Args:
            self (Director): an instance of Director.
        """
        self._terminalService.letter = str(input('Guess a letter [a-z]: ').lower())
        letter = self._terminalService.letter
        valid = self._letter_checker.letter_check(letter)
        while valid!=2:
            self._terminalService.letter = str(input('Guess a letter [a-z]: ').lower())
            letter = self._terminalService.letter
            valid = self._letter_checker.letter_check(letter)
        self._letter_checker.letters.append(self._terminalService.letter)

    def _do_updates(self):
        """Keeps watch on where the game is heading.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminalService.print_board()

        # If no more "_" left in the board means the user win the game. Then congra the user.
        if "_" not in self._terminalService._board_list:
            self._is_playing = False 
            print(f"Congrats you win!\nThe word was {self._terminalService.word.capitalize()}.")

        # Keep track of the chances that the player has left. 
        if self._terminalService.chances == 0:
            self._is_playing = False
    

    
    
        
        

    