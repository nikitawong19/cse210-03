class Letters:
    def __init__(self):
        self.letters = []

    def letter_check(self, letter):
        if letter in self.letters:
            print("Please guess a new letter you've already guessed that letter.")
            _guess = 1
            return _guess
        else:
            self.letters.append(letter)
            _guess = 2
            return _guess
