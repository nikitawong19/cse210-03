from dataclasses import replace


class terminalService:
    """"""

    def __init__(self):
        """"""
        self._chances = 4

    def read_input(self):
        """Ask the user what letter they choose"""
        letter = input("Enter a letter: ")
        return letter

    def add_word(self, word):
        """This will set the amount of lines the game board needs displayed."""

        length = int(len(word))

        for i in range(length):
            print("_", end=" ")
        print()

        word_list = []
        for i in range(1, length + 1):
            start = i - 1
            letter = slice(start, i)
            word_list.append(word[letter])

        return word_list
    
    def edit_board(self, letter, word_list):
        """If the letter was correct, edit the board"""

        if letter in word_list:
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

    def print_board(self, word, letter=""):
        """This will take the other methods and print a game board"""

        chosen_word = self.add_word(word)
        chosen_letter = self.edit_board(letter, chosen_word)
        print(chosen_letter)

        if chosen_letter == -1:
            self._chances = self._chances - 1
            print(self._chances)

        first = " ___ "
        second = "/___\\"
        third = "\   /"
        fourth = " \ / "

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
            
            

        

self = terminalService()
# self.print_body()
self.print_board("polly", letter="r")
self.print_board("polly", letter="r")
self.print_board("polly", letter="r")
self.print_board("polly", letter="r")
self.print_board("polly", letter="r")
    
    