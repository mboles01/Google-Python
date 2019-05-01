#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
#import commands

"""Copy Special exercise
"""

#directory_name = '/Users/michaelboles/Michael/Coding/2019/Google-Python/google-python-exercises/copyspecial'

# Write functions and modify main() to call them

def get_special_paths(directory_name):
    
    files = os.listdir(directory_name) # create array with filenames contained in given directory
    special_paths = []                 # initiate empty array to populate in for loop

    for file in files:                         # loop over files in directory
        special = re.search(r'(\w+__\w+__\.\w+)', file) 
                                               # find: '(letters)(__)(letters)(__)(.)(letters)'
        if special:
            special_filename = special.group(1)
                                               # if match found, create string object of filename
            special_path = os.path.abspath(os.path.join(directory_name, special_filename))
                                               # then join path of directory and file 
            special_paths.append(special_path) # tack onto end of existing path list
    return(special_paths)

#get_special_paths(directory_name)

#paths = special_paths
#destination = '/Users/michaelboles/Desktop/Copyspecial'

def copy_to(paths, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for path in paths:
        basename = os.path.basename(path)
        if not os.path.exists(os.path.join(destination, basename)):
            shutil.copy(path, os.path.join(destination, basename))
        
#def zip_to(paths, zip_path):
    

def main():
    
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
    del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
