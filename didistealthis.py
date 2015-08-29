import re
import requests
"""
Author: -zYMTOM'
Contact: https://keybase.io/mememaster
Description: Software for detecting wether or not a program has been plagiarized.
The script will search for keyphrases, variable names and lines of code to try to find it on other works.
It's not 100% accurate and is very easily bypassed by simple obfuscation, so do not rely on this.
Make sure that the person who is claiming code knows exactly what every piece of it does rather then rely on this identification.
"""

class disd(filepath, verbose, outputfile):
    def __init__(self):
		#self.file = 
        print "meme"
    def line(self):
        print "meme"
    def parse(self):
        print "xd"
if __name__ == '__main__':      
    import sys
    import argparse
    import os
    parser = argparse.ArgumentParser(prog='DidIStealThis?', usage='%(prog)s [options]')
    parser.add_argument('-f', '--file', help="Filepath to the file to check for plagirization.")
    parser.add_argument('-v', '--verbose', action='store_false', help="Gives you more info.")
    parser.add_argument('-o', '--output-file', help="Set to output the returned info into a file.")
    args = parser.parse_args()
    if args.file is not None and len(args.file) > 0:
        filepath = args.file
    else:
        filepath = raw_input("Input the path to your file")
    if not os.path.exists(filepath):
        sys.exit("File doesn't exist, supply a correct file")
    if args.verbose 
    x = disd(filepath, )