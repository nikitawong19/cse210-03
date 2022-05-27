class Letters:
    """A Letter is an alphabet enter by the user.
    
    The responsibility of a Letter is to keep track the alphabet enter by the user.
    """
    def __init__(self):
        """Constructs a new instance of Letters.
        
        Args:
            self (Letters): An instance of Letters.
        """
        # A list of alphabet.
        self._alphabet =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ""]
        
        # Put the guessed letter in an empty list.
        self._letters = []

    def letter_check(self, _letter):
        """Starts the game by running the main game loop.
        
        Args:
            self (Letter): An instance of Letters.
            letter (string): A letter entered by the user.
        """
        # If guessed letter not in the alphabet list.
        if _letter not in self._alphabet:

            # Ask the user to guess a letter.
            print("Please guess a letter.")
            _guess = 1
            return _guess
        
        # If user guess the same letter again.
        if _letter in self._letters:

            # Ask the user to guess again.
            print("You've already guessed that letter. Please guess a new letter.")
            _guess = 1
            return _guess
        
        # If the user guess correct letter, append the letter to the letter list.
        else:
            self._letters.append(_letter)
            _guess = 2
            return _guess
