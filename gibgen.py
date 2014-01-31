#Gibberish Generator

#Program to scaramble the letters of a word around, except the first and last letter.

import random
import sys
import time
<<<<<<< HEAD
=======

#Variable to hold the time the program starts

time_beg = time.time()
>>>>>>> feature

#A list to hold the words entered by the user.
time_beg = time.time()

user_input = sys.argv



"""String object to hold the list objects. I did this to eliminate any quotations used
    in the command line arguments. Otherwise, my program was treating any sentence in
    quotes as one long word instead of separate words."""
    
string = " ".join(user_input)



#New list object to hold the words to be scrambled.

list = string.split(' ')



#An empty list to hold the new gibberish words.

gibberish_words = []




"""Function to scramble the words without punctuation, leaving the first and
    last letter alone.Words with three or less letters are not scrambled.
   @require word != null
   @ensure non-gibberish_word[0] == gibberish_word[0] &&
           non-gibberish_word[-1] == gibberish_word[-1]"""

def scramble(word):

    gibberish = ""

    if len(word) == 4:

        first = word[0]

        second = word[1]

        third = word[2]

        fourth = word[3]

        gibberish = first + third + second + fourth

    else:

        first = word[0]

        middle = word[1:-1]

        last = word[-1]

        jumble = random.sample(middle, len(middle))

        new = "".join(jumble)

        gibberish = first + new + last

    return gibberish


"""Function to take a word with a hyphen or apostrophe, split it into two seperate
    words without the punctuation, scramble each new word, and then concatenate it
    back into a hyphenated word or contraction.Words with a comma in them are
    assumed to be numbers, and simply added to the list without scrambling.
   @require word != null
   @ensure  hyphenated-word = scrambled(hyphenated) + "-" + scrambled(word)
            contra'ction = scrambled(contra) + " ' " + scrambled(ction)"""


def scramblepunctmid (word):

    new = ""

    if (word.find("-") != -1):

        hyp = word.split('-')

        new = scramble(hyp[0]) + "-" + scramble(hyp[1])

    elif (word.find("'") != -1):

        apos = word.split('\'')

        new = scramble(apos[0]) + "'" + apos[1]

    else:

        new = word
        
    return new

"""Function to scramble a word with an open parentheses at the beginning. It will
    hold the parentheses in a string object, pass the word to the scramble function,
    concatenate the parentheses and the new scrambled word, and return the new word.
   @require word != null
   @ensure (word = ( + scrambled(word) = (wrod"""

def scramblepunctbeg(word):

    gibberish = ""

    if len(word) == 5:

        punct = word[0]

        new = scramble(word[1:])

        gibberish = punct + new

    else:

        first = word[0]

        sec = word[1]

        middle = word[2:-1]

        last = word[-1]

        jumble = random.sample(middle, len(middle))

        new = "".join(jumble)

        gibberish = first + sec + new + last

    return gibberish



"""Function to scramble a word while leaving the first and last letter in place, as
    well as any end punctuation. It holds the punctuation in a string object, calls
    the scramble method on the word, and then concatenates it back into a scrambled
    word with the end punctuation.
   @require word != null
   @ensure scrambled! = smalbercd!"""

def scramblepunctend(word):

    gibberish = ""

    if len(word) == 5:

        punct = word[-1]

        new = scramble(word[0:4])

        gibberish = new + punct

    else:

        first = word[0]

        middle = word[1:-2]

        seclast = word [-2]

        last = word[-1]

        jumble = random.sample(middle, len(middle))

        new = "".join(jumble)

        gibberish = first + new + seclast + last

    return gibberish

    
    


"""Iterates through the words in user_input. If the word is three letter long or less,
    it adds it to the new gibberish_words list. If the word is not hyphenated, it scrambles
    word and adds it to the new list.If the word is hyphenated, it calls scramble_hyp(word)
    and adds the hyphenated gibberish word to the new list."""

for item in list[1:]:

    if len(item) <= 3:

        gibberish_words.append(item)

    elif (item.isdigit()):

        gibberish_words.append(item)

    elif (item[0] == '('):

        gibberish_words.append(scamblepunctbeg(item))


    elif (item[-1] == '.' or item[-1] == '!' or item[-1] == '?' or item[-1] == ',' or
          item[-1] == ')'):

        gibberish_words.append(scramblepunctend(item))


    elif (item.find("-") != -1 or item.find("'") != -1 or item.find(",") != -1):

        gibberish_words.append(scramblepunctmid(item))

    else:

        gibberish_words.append(scramble(item))
        

#Converts list items into a string to be printed to the screen.

new_words = " ".join(gibberish_words)

time_end = time.time()


print(new_words)
print("Execution time in sec: ")
print(time_end - time_beg)

#Variable to hold when program finishes

time_end = time.time()

print("Execution in sec: ")
print(time_end - time_beg)




    
