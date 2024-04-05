import re
import requests
import logging
import sys
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
sys.path.append('~/.local/pypack/lib/python2.7/site-packages/')
requests.packages.urllib3.disable_warnings()
class disd():
    def __init__(self, filepath, outputfile):
        self.file = filepath
        self.outputfile = outputfile
        self.keywords = {}
        self.websites = {}
        self.found = {}
        logging.info('Starting to check '+ self.file + ' for plagiarization')
    def check(self):
        self.getFile() #Get the file to check
        self.getFormat() #Get the format, which is necessary for the regex's
        self.findKeywords() #Find the keywords using the regex
        self.search() #Google the keywords
        
    def getFile(self):
        file = open(self.file, 'r')
        self.filecontent = file.read()
        self.filebyline = file.readlines()
    def findKeywords(self):
        logging.info("Parsing the file...")
        regexs = self.getRegex()
        for reg in regexs:
            find = re.findall(reg, self.filecontent)
            for f in find:
                linefound = ""
                counter = 0
                for line in self.filebyline:
                    if f in x:
                        break
                    counter = counter + 1
                self.keywords[f] = {'checked':False, 'line':counter}
                logging.info("Keyword '"+f+"' found")
    def search(self):
        for x in self.keywords: #Loop through keywords and request them to google
            r = requests.get("https://www.google.se/search?q=\""+x+"\"", verify=False)
            found = re.findall(r'<li class="g">.*?<cite>(.*?)<\/cite>', r.content)
            for f in found:
                self.websites[websites] = x
            self.keywords[x]['checked'] = True
        for x in self.websites:  #Loop through the websites just retrieved. Should probably be handled in a separate thread or something
            r = requests.get(x, verify=False)
            for y in self.keywords:
                if y in r.content:
                    for line in r.content.split("\n"):
                        if y in line:
                            self.found[y] = {}
    def getFormat(self):
        r = re.search(r'\.([A-z]{1,5})$', self.file)
        try:
            logging.info('Fileformat found, ' + r.group(1))
            self.format = r.group(1)
            return r.group(1)
        except Exception:
            logging.info('Fileformat could not be retrieved')
            return False
    def getRegex(self, ff=None):
        logging.info('Retrieving regex...')
        regex = {
            'py' : [
                r'(\w*?)\W?=',
                r'(["\'].*["\'])',
                r'(#.*?\n|\r)',
                r'(""".*?""")'
            ],
            'php' : [
                r'(\$.*?)\W?=',
                r'(["\'].*?[\'"])',
                r'(\/\/.*?\n|\r)',
                r'(\/\*.*?\*\/)'
            ]
        }
        if self.format in regex:
            logging.info('Retrieved regex for format ' + self.format)
            return regex[self.format]
        else:
            logging.info('Could not retrieve regex for format ' + self.format)
            return false
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
    x.check()