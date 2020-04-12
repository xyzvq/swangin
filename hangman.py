import random

WORD_LIST = random.choice(open("Documents/dict.txt").read().split())

GUESS_WORD = []
HANG_WORD = (WORD_LIST)
LENGTH_WORD = len(HANG_WORD)
ALPHA = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
LETTER_STORAGE = []

def CONCEAL ():
    for i in HANG_WORD:
        GUESS_WORD.append("-")
    print("Word to guess: {0}".format(" ".join(GUESS_WORD)))

def GUESSING():
    GUESS_COUNT = 0

    while GUESS_COUNT < len(HANG_WORD) + 5:

        guess = raw_input("\npick a letter\n")
        
        if not guess in ALPHA:
            print ("\nenter a real LETTER bozo !")
        
        elif guess in HANG_WORD:
            print ("damn rights")
            LETTER_STORAGE.append(guess)
            for i in range(0, LENGTH_WORD):
                if HANG_WORD [i] == guess:
                    GUESS_WORD[i] = guess
                    print (GUESS_WORD)
        
        elif not guess in HANG_WORD:
            print ("\nNope, Guess Again!")
            LETTER_STORAGE.append(guess)
                    
        elif guess in LETTER_STORAGE:
            print ("\nyou already guessed that LETTER dumb dumb\n")
        
        print ("letters guessed already,", LETTER_STORAGE)
            
        if not '-' in GUESS_WORD:
            print("You won!\nthe secret word was", HANG_WORD)
            break
        
        GUESS_COUNT += 1
        if GUESS_COUNT == len(HANG_WORD) + 4:
            print(" You lost :<! The secret word was", HANG_WORD)
            break



CONCEAL()
GUESSING()
