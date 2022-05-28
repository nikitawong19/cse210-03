class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the terminal.
    """
    def __init__(self):
        """Constructs a new TerminalService.
        
        Args:
            self (TerminalService): An instance of TerminalService.
        """
        self.capitals=[0]
        self.chances = 4
        self.word = ""
        self.letter = ""
        self._board_list = []
        self._word_list = []
    
    def add_word(self):
        """This will set the amount of lines the game board needs displayed.
        
        Args:
            self (TerminalService): An instance of TerminalService.
        """
        # Count the length of the word.
        length = int(len(self.word))

        # Based on the length of the word append to the empty space "_".
        # For example: If the word consist of 5 letters, show 5 emppty spaces "_".
        for i in range(length):
            self._board_list.append("_")
        
        # From range 1 to whatever length of the word.
        # For example: 
        for i in range(1, length + 1):
            start = i - 1

            # Specify at which position to start the slicing. Default is 0 --> start. And at which position to end the slicing.
            # Then put in a variable called letter.
            letter = slice(start, i)

            # Append the letter to an empty word list.
            self._word_list.append(self.word[letter])

    def _edit_board(self, letter):
        """If the letter was correct, edit the board.
        
        Args:
            self(TerminalService: An instance of TerminalService)
            letter (string): The letter enter by the user.
        """
        # If the letter is found in the word list.
        if letter in self._word_list:

            # enumerate() is a built-in function dealing with iterators and to keep a count of iterations. 
            for index, elem in enumerate(self._word_list):

                # If element is equal to a dash "-"
                if elem =="-":
                     self._board_list[index] = "-"

                     # Apend the 
                     self.capitals.append(index + 1)

                if elem == letter:

                    # If index is in the 
                    if index in self.capitals:

                        # Capitalize the first letter in the word list.
                        self._board_list[index] = self._word_list[index].capitalize()

                        # Else, remain small letter.
                    else:
                        self._board_list[index] = self._word_list[index]
            
            return 0
        elif letter == "":
            return 1
        else:
            return -1
        
    def _print_body(self, dead=False):
        """Print the body of the jumper.
        
        Args:
            self (TerminalService): An instance of TerminalService.
            dead (boolean): Whether or not the jumper dead. 
        """
        # If the jumper is dead, print the body of the jumper and show the user the correct word.
        if dead:
            print("  X  ")
            print(" /|\ ")
            print(" / \ ")
            print(f"The word was {self.word.capitalize()}.")

        # If the jumper is still alive, print the body of the jumper in this manner.
        else:
            print("  0  ")
            print(" /|\ ")
            print(" / \ ")

    def _print_board(self):
        """This will take the other methods and print a game board.
        
        Args:
            self (TerminalService): An instance of TerminalService.
        """
        # A chosen letter from the edit board.
        chosen_letter = self._edit_board(self.letter)

        # Count the total number from the board list.
        for i in range(len(self._board_list)):

            # Print the board list and end with a space.
            print(self._board_list[i], end=" ")

        print()

        # If the letter is positioned last.
        if chosen_letter == -1:

            # The chances are minus one.
            self.chances = self.chances - 1

        # This is the frame for the jumper's parachute.
        first = " ___ "
        second = "/___\\"
        third = "\   /"
        fourth = " \ / "

        print()

        # If 4 chances left, print frames 1,2,3,4 for the jumper's parachute.
        if self.chances == 4:
            print(first)
            print(second)
            print(third)
            print(fourth)
            # Print the jumper's body also.
            self._print_body()

        # If 3 chances left, print frames 2,3,4 for the jumper's parachute.
        elif self.chances == 3:
            print(second)
            print(third)
            print(fourth)
            # Print the jumper's body also.
            self._print_body()

        # If 2 chances left, print frames 3,4 for the jumper's parachute.
        elif self.chances == 2:
            print(third)
            print(fourth)
            # Print the jumper's body also.
            self._print_body()

        # If 1 chances left, print frame 4 for the jumper's parachute.
        elif self.chances == 1:
            print(fourth)
            # Print the jumper's body also.
            self._print_body()

        # Else, print the jumper's body if the jumper is dead.
        else: 
            self._print_body(True)

        print()
    