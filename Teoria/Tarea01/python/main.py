#!/usr/bin/python
""" Weather consultant
Author: Angel Christian Pimentel Noriega    
Consults the weather using a web api(Open Weather)
This module calls class reader to read the csv file sent through the command line
This script requires a file (.csv)
functions:
  * main - the main function of the script, makes an instance of Reader an reads 
           the csv file
"""
import sys
from classes.reader import reader

def main():
  if len(sys.argv) == 2:
    try:
      reader_ = reader(sys.argv[1])
      reader_.read()
    except FileNotFoundError:
      sys.exit("Invalid file, try again")
  else:
    sys.exit("USE > python3 main.py [file]")

if __name__ == "__main__":
    main()
