from game.word_bank import Words
from game.letter_checker import Letters
from game.terminal_service import TerminalService

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
        """Constructs a new instance of Director.
        
        Args:
            self (Director): An instance of Director.
        """
        self._word_bank = Words()
        self._letter_checker = Letters()
        self._terminalService = TerminalService()
        self._terminalService.word = self._word_bank.random_word().lower()
        self._terminalService.add_word()
        self._is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): An instance of Director.
        """
        # As long as the game is not over, continue to get input and do update.
        while self._is_playing:
            self._get_inputs()
            self._do_updates()

    def _get_inputs(self):
        """Ask the user to guess a letter.

        Args:
            self (Director): An instance of Director.
        """
        # Ask the user to guess a letter.
        self._terminalService.letter = str(input('Guess a letter [a-z]: ').lower())

        # Put the letter in a variable.
        letter = self._terminalService.letter

        # Check to see if the letter is valid.
        valid = self._letter_checker.letter_check(letter)

        # If the letter is invalid, continue to ask the user for a letter again.
        while valid!=2:
            self._terminalService.letter = str(input('Guess a letter [a-z]: ').lower())

            # Put the letter in a variable.
            letter = self._terminalService.letter

            # Check to see if the letter is valid.
            valid = self._letter_checker.letter_check(letter)

        # If the letter is valid, append it to the letter list.
        self._letter_checker._letters.append(self._terminalService.letter)

    def _do_updates(self):
        """Updates the player if they guess successfully. Keeps watch on where the game is heading.
        
        Args:
            self (Director): An instance of Director.
        """
        # Print the body of the jumper.
        self._terminalService._print_board()

        # If there is no more empty space "_" on the board, the user has won the game. Then congratulations to the user.
        if "_" not in self._terminalService._board_list:

            # If the user wins, the game is over.
            self._is_playing = False 

            # Print both the congratulations message and the correct word.
            print(f"Congrats you win!\nThe word was {self._terminalService.word.capitalize()}.")

        # If the chances reach zero, the game is over.
        if self._terminalService.chances == 0:
            self._is_playing = False
    

    
    
        
        

    