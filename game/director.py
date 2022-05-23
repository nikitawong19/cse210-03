from game.word_bank import Words
from game.letter_checker import Letters
from game.terminalService import terminalService
import random

class Director:
    def __init__(self):

        self._word_bank = Words
        # self._letter_checker = Letters
        self._terminalService = terminalService
        self._is_playing = True

    def start_game(self):
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            # self._do_outputs()
    
    def _get_inputs(self):
        while self._is_playing:
            self.user_input = input('Guess a letter [a-z]: ')
            return self.user_input
        
        
    def _do_updates(self):
        words = ['january', 'february', 'march']
        self.random_word = random.choice(words)

        wrong_letter_count = 0

        for self.random_word in self.random_word:
            if self.user_input in self.random_word:
                print(self.user_input, end=' ')
            else:
                print('_', end=' ')
                wrong_letter_count = wrong_letter_count + 1 # If guess wrong, increase failure count by 1.
        print('')
    
        # failure_count = 6
        

        # # As long as the failure count is less than zero the game will keep going. Else, the game can continue.
        # while failure_count > 0:
        #     if wrong_letter_count == 0:
        #         print('You won.')
        #         break # If failure count still remain 0, break out from the loop.


        # if self.user_input in self.random_word:
        #     print('Correct guess.')
        # else:
        #     print(f'Incorrect. {failure_count} turn left.')
        #     failure_count = failure_count - 1 # If guess correct, decrease failure count by 1.

        # Whole collection of letter that has been guessed.
        # letter_guessed = letter_guessed + self.user_input
        
        

    