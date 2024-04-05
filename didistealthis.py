import re
import requests
import logging
"""
didistealthis.py
Version: 0.0 - Still in development
Author: -zYMTOM'
Contact: https://keybase.io/mememaster
Description: Software for detecting wether or not a program has been plagiarized.
The script will search for keyphrases, variable names and lines of code to try to find it on other works.
It's not 100% accurate and is very easily bypassed by simple obfuscation, so do not rely on this.
Make sure that the person who is claiming code knows exactly what every piece of it does rather then rely on this identification.
"""

class disd():
    def __init__(self, filepath, outputfile):
        self.file = filepath
        self.outputfile = outputfile
        
    def line(self):
        print "meme"
    def parse(self):
        print "xd"
    def getFormat(self):
        
if __name__ == '__main__':      
    import sys
    import argparse
    import os
    
    parser = argparse.ArgumentParser(prog='DidIStealThis?', usage='%(prog)s [options]')
    parser.add_argument('-f', '--file', help="Filepath to the file to check for plagirization.")
    parser.add_argument('-v', '--verbose', action='store_false', help="Gives you more info.")
    parser.add_argument('-o', '--outputfile', help="Set to output the returned info into a file.")
    args = parser.parse_args()
    
    filepath = None
    outputfile = None
    
    if args.file is not None and len(args.file) > 0:
        filepath = args.file
    else:
        filepath = raw_input("Input the path to your file")
    if not os.path.exists(filepath):
        sys.exit("File doesn't exist, supply a correct file")
    if args.outputfile is not None and len(args.outputfile) > 0:
        outputfile = args.outputfile
    else:
        outputfile = "logs.txt"
    level = logging.INFO
    if args.verbose:
        level = logging.DEBUG
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', filename=outputfile, level=level)
    x = disd(filepath, outputfile)