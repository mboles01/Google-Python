#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import sys, os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Google-Python')
filename = 'Alice.txt'

#def open_file(filename):
#    content_temp1 = open(filename, 'r').read()
#    content_temp2 = content_temp1.lower()
#    text = content_temp2.split()
#    return text

def mimic_dict(filename):
    """Given text file, generate dictionary with key - values: word - following words"""
    content_temp1 = open(filename, 'r').read()
    content_temp2 = content_temp1.lower()
    text = content_temp2.split()    
    mimic_dict = {}                             # create empty dictionary
    current_key = ''                            # seed with empty string as first key
    for word in text:                           # loop over list of words
        if not current_key in mimic_dict:       # if key not in dict, add key-value pair
            mimic_dict[current_key] = [word]
        else:
            mimic_dict[current_key].append(word) # otherwise add value to existing key
            current_key = word                  # advance one word within list of words
    return mimic_dict, text

#mimic_dict('Alice.txt')

def print_mimic(mimic_dict, text):
    """Given mimic dict and start word, prints 200 random words."""
    import random
    word = random.choice(text)
    mimic_list = [word]                           # start with seed word in mimic list
    for index in range(199):                      # do the following 200 times:
        next_words = mimic_dict[word]             # for seed word, look up following words
        next_words_choice = random.choice(next_words) # choose one of those to be next
        mimic_list.append(next_words_choice)      # add choice to end
        word = next_words_choice                  # stage this last word for mimic dict lookup
    mimic_list2 = ' '.join(mimic_list)
    print(mimic_list2)

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
