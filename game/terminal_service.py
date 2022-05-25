class terminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the terminal.
    """
    def __init__(self):
        """"""
        self.capitals=[0]
        self.chances = 4
        self.word = ""
        self.letter = ""
        self._board_list = []
        self._word_list = []
    
    def add_word(self):
        """This will set the amount of lines the game board needs displayed."""

        length = int(len(self.word))

        for i in range(length):
            self._board_list.append("_")
        
        for i in range(1, length + 1):
            start = i - 1
            letter = slice(start, i)
            self._word_list.append(self.word[letter])
    
    def _edit_board(self, letter):
        """If the letter was correct, edit the board"""

        if letter in self._word_list:
            for index, elem in enumerate(self._word_list):
                if elem =="-":
                     self._board_list[index] = "-"
                     self.capitals.append(index + 1)
                if elem == letter:
                    if index in self.capitals:
                        self._board_list[index] = self._word_list[index].capitalize()
                    else:
                        self._board_list[index] = self._word_list[index]
            
            return 0
        elif letter == "":
            return 1
        else:
            return -1
        
    def _print_body(self, dead=False):
        """Print the body of the jumper"""

        if dead:
            print("  X  ")
            print(" /|\ ")
            print(" / \ ")
            print(f"The word was {self.word.capitalize()}")
        else:
            print("  0  ")
            print(" /|\ ")
            print(" / \ ")

    def print_board(self):
        """This will take the other methods and print a game board"""

        chosen_letter = self._edit_board(self.letter)

        for i in range(len(self._board_list)):
            print(self._board_list[i], end=" ")
        print()
        if chosen_letter == -1:
            self.chances = self.chances - 1

        first = " ___ "
        second = "/___\\"
        third = "\   /"
        fourth = " \ / "

        print()

        if self.chances == 4:
            print(first)
            print(second)
            print(third)
            print(fourth)
            self._print_body()
        elif self.chances == 3:
            print(second)
            print(third)
            print(fourth)
            self._print_body()
        elif self.chances == 2:
            print(third)
            print(fourth)
            self._print_body()
        elif self.chances == 1:
            print(fourth)
            self._print_body()
        else:
            self._print_body(True)

        print()
    