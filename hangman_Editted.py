# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



#########TEST WORDS, GUESS-LIST
#secret_word = 'apple' #choose_word(wordlist)#
#letters_guessed = ['a', 'i', 'k', 'p', 'e'] #['e', 'i', 'k', 'p', 'r', 's']


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guess_result = [] #initialize list to store comparison result
    for letter in secret_word:
        check = letter in letters_guessed
        if check:
            guess_result.append(check)
            
#    print(guess_result)
    
    if len(guess_result) == len(secret_word):
        return True
    else:
        return False
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guess_result = '' #initialize string to store correct guesses
    for letter in secret_word:
        check = letter in letters_guessed
        if check:
            guess_result += letter
        else:
            guess_result += '_ '
    return guess_result



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    for letter in letters_guessed:
        check = letter in letters
        if check:
            letters = letters.replace(letter, '')
    return letters
            
            
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    #Initialize number of guesses variable, n
    n = 6
    
    #define available letters
    available_letters = string.ascii_lowercase
    
    #number of warnings, m
    m = 3
    
    #initialize warnings
    warnings = m
    
    #initialize guess_list
    player_guess = []
    
    #initialize list to store unique guesses
    unique_letters = []
    
    #initialize counter
    counter = 0
    
    #initialize vowels
    vowels = 'aeiou'
    
    while n > 0:
        counter +=1
        if counter == 1:
            print('You have', warnings, 'warnings left!')
        print('----------------------------')    
        if n == 1:
            print('You have', n, 'guess left!')
        else:
            print('You have', n, 'guesses left!')
        
        print('Available letters:', available_letters)
        guess = input('Please guess a letter: ')
        guess = guess.lower()
        
        if guess in player_guess:
            if warnings > 0:
                warnings -= 1
                guessed_word = get_guessed_word(secret_word, player_guess)
                print('Ooops! You\'ve already guessed that letter! You now have', warnings, 'warning(s):', guessed_word)
            elif warnings == 0:
                warnings = m #reset warning
                n -= 1 #update number of guesses
                guessed_word = get_guessed_word(secret_word, player_guess)
                print('Ooops! You\'ve already guessed that letter! You have no warnings left so you lose one guess:', guessed_word)
        
        elif guess.isalpha():
            player_guess.append(guess) #Add player's guesses to 'player_guess' list
            guessed_word = get_guessed_word(secret_word, player_guess)
            if guess in secret_word:
                unique_letters.append(guess)
                print('Good guess:', guessed_word)
            else:
                print('Oops! That letter is not in my word:', guessed_word)
                if guess in vowels:
                    n -= 2
                else:
                    n -= 1
                
        elif guess.isalpha()== False and warnings > 0:
            guessed_word = get_guessed_word(secret_word, player_guess)
            warnings -= 1
            print('That is not a valid letter. You have', warnings, ' warning(s) left:', guessed_word)
                
        else: #guess.isalpha()== False and warnings == 0
            guessed_word = get_guessed_word(secret_word, player_guess)
            n -= 1
            print('That is not a valid letter. You have no warnings left so you lose one guess:', guessed_word)
            warnings = m
                

        available_letters = get_available_letters(player_guess)
        
        
        if is_word_guessed(secret_word, player_guess):
            total_score = n * len(unique_letters)
            print('----------------------------')  
            print('Congratulations! You won!')
            print('Your total score for this game is:', total_score)
            break
    if is_word_guessed(secret_word, player_guess) == False:
        print('----------------------------')  
        print('Sorry, you ran out of guesses! The word was', secret_word)
        
        
    




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


#######3A
#Test case
#secret_word = 'apple' #choose_word(wordlist)#
#letters_guessed = ['a', 'i', 'k', 'p', 'e'] #['e', 'i', 'k', 'p', 'r', 's']

#my_word = secret_word #get_guessed_word(secret_word, letters_guessed)
#other_word = 'abbbbcc'


        
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word2 = my_word.replace(' ', '')
    
    if len(my_word2) != len(other_word):
        comparison = False
    
    else:
        for idx, letter in enumerate(my_word2):
            if letter == '_':
                continue
            
            elif my_word2.count(letter) != other_word.count(letter):
                comparison = False
                break
            
            
            else:
                comparison = my_word2[idx] == other_word[idx]
                if comparison:
                    continue
                else:
                    break
    return comparison
                

#test = match_with_gaps(my_word, other_word)



#######3B
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_words = []
    for word in wordlist:
        match = match_with_gaps(my_word, word)
        if match:
            possible_words.append(word)
    if len(possible_words) == 0:
        print('No matches found!')
    else:
        print(possible_words)
        
            
        



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    #Initialize number of guesses variable, n
    n = 6
    
    #define available letters
    available_letters = string.ascii_lowercase
    
    #number of warnings, m
    m = 3
    
    #initialize warnings
    warnings = m
    
    #initialize guess_list
    player_guess = []
    
    #initialize list to store unique guesses
    unique_letters = []
    
    #initialize counter
    counter = 0
    
    #initialize vowels
    vowels = 'aeiou'
    
    while n > 0:
        counter +=1
        if counter == 1:
            print('You have', warnings, 'warnings left!')
        print('----------------------------')    
        if n == 1:
            print('You have', n, 'guess left!')
        else:
            print('You have', n, 'guesses left!')
        
        print('Available letters:', available_letters)
        guess = input('Please guess a letter: ')
        guess = guess.lower()
        
        if guess == '*':
            guessed_word = get_guessed_word(secret_word, player_guess)
            show_possible_matches(guessed_word)
            
        elif guess in player_guess:
            if warnings > 0:
                warnings -= 1
                guessed_word = get_guessed_word(secret_word, player_guess)
                print('Ooops! You\'ve already guessed that letter! You now have', warnings, 'warning(s):', guessed_word, '.')
            elif warnings == 0:
                warnings = m #reset warning
                n -= 1 #update number of guesses
                guessed_word = get_guessed_word(secret_word, player_guess)
                print('Ooops! You\'ve already guessed that letter! You have no warnings left so you lose one guess:', guessed_word, '.')
        
        elif guess.isalpha():
            player_guess.append(guess) #Add player's guesses to 'player_guess' list
            guessed_word = get_guessed_word(secret_word, player_guess)
            if guess in secret_word:
                unique_letters.append(guess)
                print('Good guess:', guessed_word)
            else:
                print('Oops! That letter is not in my word:', guessed_word, '.')
                if guess in vowels:
                    n -= 2
                else:
                    n -= 1
                
        elif guess.isalpha()== False and warnings > 0:
            guessed_word = get_guessed_word(secret_word, player_guess)
            warnings -= 1
            print('That is not a valid letter. You have', warnings, ' warning(s) left:', guessed_word, '.')
                
        else: #guess.isalpha()== False and warnings == 0
            guessed_word = get_guessed_word(secret_word, player_guess)
            n -= 1
            print('That is not a valid letter. You have no warnings left so you lose one guess:', guessed_word, '.')
            warnings = m
                

        available_letters = get_available_letters(player_guess)
        
        
        if is_word_guessed(secret_word, player_guess):
            total_score = n * len(unique_letters)
            print('----------------------------')  
            print('Congratulations! You won!')
            print('Your total score for this game is:', total_score, '.')
            break
    if is_word_guessed(secret_word, player_guess) == False:
        print('----------------------------')  
        print('Sorry, you ran out of guesses! The word was', secret_word, '.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
