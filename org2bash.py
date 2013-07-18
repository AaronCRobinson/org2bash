#!/usr/bin/python
import argparse

def main():
   parser = argparse.ArgumentParser(description="This program does magic.")
   parser.add_argument('org_file', type=argparse.FileType('r'))
   args = parser.parse_args()

   shell = False

   for line in args.org_file:
      # change flag when necessary
      if line.startswith('#+BEGIN_SRC sh'): shell=True; continue
      elif line.startswith('#+END_SRC'): shell=False; continue

      # if this is a shell command  that is not a comment, then print
      # NOTE: get rid of extra newline
      if shell == True and line[0] != '#': print line[:-1]

if __name__=="__main__":
   main()
