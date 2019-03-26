# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False 
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ""
    for i in range(len(secretWord)):
        l = secretWord[i]   
        if l in lettersGuessed:
            guessedWord += l
        else:
            guessedWord += "_ "        
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    alphabet = list(string.ascii_lowercase)
    
    for letter in lettersGuessed:
        alphabet.remove(letter)
        
    availableLetters = ''.join(alphabet)
    return availableLetters
  
    

def success(secretWord):
    print()
    print("You successfully guessed secret word",secretWord)
    print("CONGRATULATIONS!")
    enter = input()
    return newRound()



def failure(secretWord):
    print()
    print("No chances left...")
    print("YOU ARE HANGED!")
    print()
    print("It was -",secretWord.upper(),"- all the time.")
    enter = input()
    return newRound()



def newRound():
    print("New round?")
    while True:
        user = input("Y/N: ")
        user = user.lower()
        if user == "y":
            secretWord = chooseWord(wordlist).lower()
            return hangman(secretWord)
        if user == "n":
            return



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print()
    print("----------------------------------------------------------------")
    print("Welcome to Hangman Game")
    print()
    print("The goal is to guess the secret word, one character at the time.")
    print("Failing EIGHT times will get you hanged.")
    print()
    print("Best of luck!")
    print("----------------------------------------------------------------")
    print()
    print("This time you need to guess",len(secretWord),"letters")
    

    chancesLeft = 8
    lettersGuessed = []

    while True:
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        availableLetters = getAvailableLetters(lettersGuessed)
        
        enter = input()
        print()
        print()
        print("Secret word:",guessedWord)
        print()
        print("Letters available:",availableLetters)
        print("Chances left:",chancesLeft)
        guess = input("Supply a guess: ")
        guess = guess.lower()
        print()
        print()
        if guess not in availableLetters:
            print("You should choose an available letter!")
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("GOOD GUESS!")
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    return success(secretWord)
            else:
                chancesLeft -= 1
                print("YOU MISSED!")
                if chancesLeft == 0:
                    return failure(secretWord)
                

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
                    

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
