#Mystery Word
##Implement the game of Mystery Word.
###Objectives
After completing this assignment, you should...

- Understand all the basics of Python!
- Be able to create an interactive program.
- Be able to choose a random value.
- Be able to keep track of state.
- Be able to read from a file.
- Be able to test your code.

###Deliverables
- A Git repo named mystery-word containing at least:
- A README.md file with a description that also explains how to run your project.
- Your main function and supporting functions in mystery_word.py.
- A suite of tests for your project in mystery_word_test.py.

####Normal Mode
You will implement the game Mystery Word. In your game, you will be playing against the computer.

The computer must select a word at random from the list of words in the file /usr/share/dict/words. This file exists on your computer already.

The game must be interactive; the flow of the game will go as follows:

Let the user choose a level of difficulty at the beginning of the program. Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.
At the start of the game, let the user know how many letters the computer's word contains.
Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it does not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.
Let the user know if their guess appears in the computer's word.
Display the partially guessed word, as well as letters that have not been guessed. For example, if the word is BOMBARD and the letters guessed are a, b, and d, the screen would display:
B _ _ B A _ D
A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.

A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess.

If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.

The game will end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.

When a game ends, ask the user if they want to play again. The game begins again if they reply positively.

####Requirements
- Write functions to select a subset of the complete word list.
- Write a function to select a word at random from the word list.
- Write a function to display a word with blanks/letters filled in the appropriate spots.
- Write a function to check if a word has been completely guessed.
- Write other helper functions as necessary to help with the flow of the game.
- Run mystery_word_test.py and ensure you pass all the unit tests.

####Advanced Mode (optional)
- Implement the evil version of this game.
- Write it in a new Python program named evil_mystery_word.py.
- Write tests for new functionality you introduce in evil_mystery_word_tests.py.

####Notes
When testing, keep in mind that testing user input and output is hard. Testing functions that have no side-effects -- that is, they take some arguments and return a value without getting information from input() or using random -- is much easier. Try to keep all your logic in pure functions and then have an outer crust of functions that talk to the user or read from files surrounding your delicious pure function middle. If you are able to do this, you will not need to test that outer crust.
