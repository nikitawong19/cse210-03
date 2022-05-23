from dataclasses import replace


class terminalService:
    """"""

    def __init__(self):
        """"""
        self._chances = 4
        self.word = "polly"
        self.letter = ""
        self._board_list = []
        self._word_list = []
        self.add_word()

    def read_input(self):
        """Ask the user what letter they choose"""
        self.letter = input("Enter a letter: ")
        

    def add_word(self):
        """This will set the amount of lines the game board needs displayed."""

        length = int(len(self.word))

        for i in range(length):
            self._board_list.append("_")
        
        for i in range(1, length + 1):
            start = i - 1
            letter = slice(start, i)
            self._word_list.append(self.word[letter])

        return self._word_list
    
    def edit_board(self, letter):
        """If the letter was correct, edit the board"""

        if letter in self._word_list:
            for index, elem in enumerate(self._word_list):
                if elem == letter:
                    self._board_list[index] = self._word_list[index]
            
            return 0
        elif letter == "":
            return 1
        else:
            return -1
        
    
    def print_body(self, dead=False):
        """Print the body of the jumper"""

        if dead:
            print("  X  ")
            print(" /|\ ")
            print(" / \ ")
        else:
            print("  0  ")
            print(" /|\ ")
            print(" / \ ")

    def print_board(self, letter=""):
        """This will take the other methods and print a game board"""

        chosen_letter = self.edit_board(letter)

        length = int(len(self.word))

        for i in range(length):
            print(self._board_list[i], end=" ")
        print()
        if chosen_letter == -1:
            self._chances = self._chances - 1
            print(self._chances)

        first = " ___ "
        second = "/___\\"
        third = "\   /"
        fourth = " \ / "

        print()

        if self._chances == 4:
            print(first)
            print(second)
            print(third)
            print(fourth)
            self.print_body()
        elif self._chances == 3:
            print(second)
            print(third)
            print(fourth)
            self.print_body()
        elif self._chances == 2:
            print(third)
            print(fourth)
            self.print_body()
        elif self._chances == 1:
            print(fourth)
            self.print_body()
        else:
            self.print_body(True)

        print()
            
            

        

self = terminalService()
# self.print_body()
self.print_board(letter="p")
self.print_board(letter="o")
self.print_board(letter="l")
self.print_board(letter="y")
    
    