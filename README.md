# cse210-03

terminalService
What I will need
-DIRECTOR: I will need the prompt that will read to the terminal asking what letter they chose. `read_input("\n Enter a prompt")

My methods:
add_word(word): I will use this to add the word that was chosen to the game board. This should only need to be used at the start of the game. Using a method instead of an attribute should keep me from being a class into this one. This should contribute to encapsulation.

read_input(): This will read to the terminal asking the user for the letter they pick. Referring to the seeker game, I can get the prompt from Director

edit_board(outcome): This can be used to let me know if the letter the user entered was correct or incorrect. From there I can edit the board.

add_list(lettersList): I can receive a list of the letters already guessed and add them to the list to use in the print_board() method

print_board(list): Using the list I can place the letters into the appropriate places and print the board to the console.
