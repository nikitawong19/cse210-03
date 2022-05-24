from game.word_bank import Words
from game.letter_checker import Letters
from game.terminal_service import terminalService

class Director:
    def __init__(self):
        self._word_bank = Words()
        self._letter_checker = Letters()
        self._terminalService = terminalService()
        self.word = "polly"
        self._is_playing = True

    def start_game(self):
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            # self._do_outputs()
    
    def _get_inputs(self):
        """
        Ask the user to guess a letter.
        """
        # while self._is_playing:
        self._terminalService.letter = input('Guess a letter [a-z]: ')
        self._letter_checker.letters.append(self._terminalService.letter)
        # return self.user_input
        
    def _do_updates(self):
        self._terminalService.word = self._word_bank.random_word()
        self._terminalService.print_board()
    
        for self.random_word in self.random_word:
            if self.user_input in self.random_word:
                print(self.user_input, end=' ')
            else:
                print('_', end=' ')
        print('')
    
    
        
        

    