#!/usr/bin/python

import sys
import re

def extract_names(filename):
    
  """
  Given a file name for baby<year>.html,
  returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  If this seems too daunting, return
  ['2006', (male_name,rank), (female_name,rank), ....]
  The names and ranks are pairs rather than strings and they
  do not have to be sorted. For example the list might begin
  ['2006', ('Jacob','1'), ('Emma','1'), ...]
  
  """
#open file
  f = open(filename,mode = "r",encoding = "utf-8",).read()
    
#search for year in this document
  year = re.search(">Popularity\sin\s(\d\d\d\d)<",f)[1]

  #print("The year of this file is",year)
#if cannot find year, print something and stop this function
  if not year:
        print("There is no obvious year in this file")
        sys.exit(0)
    
#search for the name
  name2 = re.findall("<td>([0-9]+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>",f)
  #print("There are {} names in this file".format(2*len(name2)))
  #if len(name2)==0:
    #print("There are no names in this file")
    
#Extract boy's name and girl's name
  name = {}
  for i in range(len(name2)):
        boy = name2[i][1]
        name[boy] = i+1
        girl = name2[i][2]
        name[girl]=i+1
    
  name_rank = []
  name_rank.append(year)
  

  sort_name = sorted(name.keys())
    
  for i in sort_name:
    name_rank.append(i+" "+str(name[i]))
        
        
  return name_rank


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.

  if len(sys.argv) == 2:
        arg = sys.argv[1]
        
  else:
        print("usage: ", sys.argv[0], "filename")
        sys.exit(1)

  # +++your code here+++
  # For each filename, get the names, then print the text output
  names = extract_names(arg)
  text = '\n'.join(names) + '\n'
    
  print(text)

  print('Yes, you are running the script correctly!')

if __name__ == '__main__':
    main()
