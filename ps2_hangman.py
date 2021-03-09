# 6.00 Problem Set 3
# 
#Hangman

#Pasit Wongsupha(Ohm) aka Ajarn
#Time: Approximately 5 hours


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print("  ", len(wordlist), "words loaded.")
    return(wordlist)

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return(random.choice(wordlist))

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def hangman_with_ajarn():
    value = raw_input("Are you one of my student? [Y/N]:")
    if value == "Y" or value == "y":
        print("Student: Let's play a game.")
        print("Ajarn: What game? I don't know any game.")
        print("Student: You know, 'that' game.")
        print("Ajarn: I think you don't know what you're talking about.")
        print("Student: Again.")
        print("Student: Let's play a game.")
        print("Ajarn: What game? I don't know any game.")
        print("Student: I know you do.")
        print("Ajarn: Ah AhAh AhAhAh AhAhAhAhAh")
        print("Student: Gasp!")
        print("Ajarn: Up da da da da dub")
        print("Student: I will be going now.")
        print("Ajarn: Bye~ Bye~")
        print("Student: Ajarn!!!!!!!!")
        print("Ajarn: Arari~~~~~~~~, Oh~~~~~~~~")
        print("Ajarn: Let's play the hangman game with Ajarn aka Pasit Wongsupha")
        hangman()
    if value == "N" or value == "n":
        print("KUY!")

def guess_str(lis_guess):
    guess = ""
    for i in lis_guess:
                guess = guess + i + " "
    return(guess)


def user_input(word,alphabets,guess,lis_word,lis_guess,n):
    if "_" not in lis_guess:
        return("Congrats, You Won!")
    if n == 0 and "_" in lis_guess:
        return("Try again next time. The word is " + word)
    else:
        ava_alpha = ""
        for i in alphabets:
            ava_alpha = ava_alpha + i
        print("You have " + str(n) + " guesses left.")
        print("Available Alphabets:"    + ava_alpha)
        x = raw_input("Please select an English language alphabet:").lower()
        if x in alphabets:
            for i in range(len(lis_word)):
                if x == lis_word[i]:
                    lis_guess[i] = x
            if x in alphabets:
                alphabets.remove(x)
            guess_str(lis_guess)
            print("Good Guess: " + guess_str(lis_guess)[:-1])
            return(user_input(word,alphabets,guess,lis_word,lis_guess,n-1))
        else:
            guess_str(lis_guess)
            print("Nice Try: " + guess_str(lis_guess)[:-1])
            return(user_input(word,alphabets,guess,lis_word,lis_guess,n-1))

def hangman():
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    guess = ""
    word = choose_word(wordlist)
    word_length = len(word)
    lis_word = [i for i in word]
    lis_guess = ["_"]*word_length
##    print(lis_word)
    print("The word contains " + str(word_length) + " letters.")
    print(user_input(word,alphabets,guess,lis_word,lis_guess,word_length*2))

hangman_with_ajarn()
