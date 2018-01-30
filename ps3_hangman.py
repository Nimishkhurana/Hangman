# hangman

import random
import string
import os

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
    count=0
    for ch in secretWord:
      if ch in lettersGuessed:
         count+=1
      else:
         break
    if count==len(secretWord):
       return True
    else:
       return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess=''
    for ch in secretWord:
      if ch in lettersGuessed:
         guess+=ch
      else:
         guess+='_'
      guess+=' '
    return guess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avail=''
    for ch in string.ascii_lowercase:
       if ch not in lettersGuessed:
          avail+=ch
    return avail


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
    f="-----------"
    ch="yes"
    while ch=="yes":
       unused_variable=os.system('cls')             #to clear screen everytime (on windows)
       guesses=8
       availableLetters=getAvailableLetters('')

       lettersGuessed=mistakesMade=[]
       print("Welcome to the game, Hangman!")
       print("I am thinking of a word that is {} letters long".format(len(secretWord)))
       print(f)
       while guesses>0:
          print(f"You have {guesses} guesses left")
          print("available letters:",availableLetters)
          guessletter=input('Please guess a letter:')
          lettersGuessed.append(guessletter)
          if guessletter in availableLetters:
              if guessletter in secretWord:
                  print("Good guess:",end='')
              else:
                  print("Oops! That leter is not in my word:",end='')
                  guesses-=1
                  mistakesMade.append(guessletter)
          else:
              print("Oops! You've already guessed that letter:",end='')
          print(getGuessedWord(secretWord,lettersGuessed))
          print(f)
          if "_" not in getGuessedWord(secretWord,lettersGuessed):
              print("Congratulations, you won")
              break
          availableLetters=getAvailableLetters(lettersGuessed)
       if guesses==0:
          print("Sorry, you ran out of guesses. The word was else.")
          print("The word was:",secretWord)
       ch=(input("Do you want to continue YES or NO\n")).lower()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
