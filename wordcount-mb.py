#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.


...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.



Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

# Then print_words() and print_top() can just call the utility function.

import sys, os, string

# os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Google\\basic') #PC
# os.chdir('/Users/michaelboles/Michael/Coding/2019/Google-Python') #mac

"""
Write a helper utility function that reads a file
and builds and returns a word/count dict for it.
"""

def wordcount_dict(filename):
    wordcount = {}
    text = open(filename, 'r')
    content = text.read()
    content2 = content.lower()
#    content3 = content2.translate(None, string.punctuation)
    content4 = content2.split()
    for word in content4:
        if not word in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] = wordcount[word] + 1
    return wordcount
                
#wordcount = wordcount_dict('Alice.txt')
    


"""
1. Implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
"""
def print_words(filename):
    wordcount = wordcount_dict(filename)
    wordcount_sorted = sorted(wordcount.keys())
    for word in wordcount_sorted:
        print(word, wordcount[word])


"""
2. Implement a print_top(filename) which is similar to print_words() 
but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
"""
import operator
filename = 'Alice.txt'
wordcount = wordcount_dict(filename)

def print_top(filename):
    wordcount = wordcount_dict(filename)
    sortedwords = sorted(wordcount.items(),key=operator.itemgetter(1),reverse=True)
    topcount = sortedwords[0:20]
    for i in range(len(topcount)):
        print(topcount[i][0], topcount[i][1])

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
