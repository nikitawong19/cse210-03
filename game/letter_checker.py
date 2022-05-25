class Letters:
    def __init__(self):
        self.letters = []
        self._alphabet =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ""]

    def letter_check(self, letter):
        if letter not in self._alphabet:
            print("Please guess a letter.")
            _guess = 1
            return _guess
        if letter in self.letters:
            print("Please guess a new letter you've already guessed that letter.")
            _guess = 1
            return _guess
        else:
            self.letters.append(letter)
            _guess = 2
            return _guess
