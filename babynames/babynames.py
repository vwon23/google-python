#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

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

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  year_name_rank = []
  f = open(filename, 'r')
  text = f.read()
  match_year = re.search(r'Popularity in (\d\d\d\d)</h3>', text)
  
  if match_year:
    year = match_year.group(1)
    year_name_rank.append(year)
  else:
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)  
  
  rank_names_tuple = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  rank_name_dict = {}
  for rank_name in rank_names_tuple:
    (rank, boyname, girlname) = rank_name
    if boyname not in rank_name_dict:
      rank_name_dict[boyname] = rank
    if girlname not in rank_name_dict:
      rank_name_dict[girlname] = rank
      
  rank_names = sorted(rank_name_dict.keys())
  for name in rank_names:
    year_name_rank.append(name + ' ' + rank_name_dict[name])
  
  return year_name_rank
  
# filename = sys.argv[1]
# print (extract_names(filename))

# sys.exit()

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    # Make text out of the whole list
    text = '\n'.join( extract_names(filename))

    if summary:
      outf = open(filename + '.summary', 'w')
      outf.write(text + '\n')
      outf.close()
    else:
      print (text)
  # LAB(end solution)
	  
    
if __name__ == '__main__':
  main()
