#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

# Point to local directory containing html file 
import sys, os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Google-Python/babynames_html')

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]

  """

  # open and read html file
  file = open(filename)
  text = file.read()
  
  # create emtpy array where baby names will be placed
  baby_names = []
  
  # extract year by matching string pattern: "Popularity in yyyy", where y = digit
  import re
  year = re.search(r'Popularity\sin\s(\d\d\d\d)',text) 
  if not year:
      sys.stderr.write('Couldn\'t find the year\n')
      sys.exit(1)
  year = year.group(1)
  baby_names.append(year)
 
  # extract rank, male, and female names matching string pattern: 
  # (any number of digits) (any number of letters) (any number of letters)
  # separated by html table <td> tags
  rank_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
  
#  loop through rank_names, building a dictionary as {key: name, value: rank}
  name_rank_dict = {}
  for tuple in rank_names:
      (rank, boy_name, girl_name) = tuple
      if boy_name not in name_rank_dict:
          name_rank_dict[boy_name] = int(rank)
      if girl_name not in name_rank_dict:
          name_rank_dict[girl_name] = int(rank)
    
#     equivalent to saying:
#     for i == 0:len(rank_names)-1:
#          (rank, boy_name, girl_name) = rank_names[i][0:3]
      
#   loop through dictionary, building list in ['name rank', 'name rank'] format 
  name_rank_list = []
  for key in name_rank_dict:
      name_rank_list.append(str(key) + ' ' + str(name_rank_dict[key]))
  return name_rank_list
 
#names = extract_names('baby1990.html')

# command line parsing code

def main():
  # Make a list of command line arguments, omitting the [0] element
  # which is the script name itself
  args = sys.argv[1:]

  # Correct user input: need at least 1 html filename, option to write summary file
  if not args:
    print('usage: [--summaryfile] file [file ...]') # need one filename, summary option
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the ranked names list
  # or write it to a summary file
  for filename in args:
    names = extract_names(filename)   

  # Make text out of the whole list
    text = '\n'.join(names)

  # If summary option selected, 
  if summary:
    output_summary = open(filename + '_summary.txt', 'w')
    output_summary.write(text + '\n')
    output_summary.close()
  else:
    print(text)
  
if __name__ == '__main__':
  main()