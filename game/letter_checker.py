class Letters:
    def __init__(self):
        self.letters = []

    def letter_check(self):
        if self.letters.lower() in self.guess.lower():
            print("Please guess a new letter you've already guessed that letter.")
            _guess = 1
            return _guess
        else:
            self.letters.append(self.guess)
            _guess = 2
            return _guess
