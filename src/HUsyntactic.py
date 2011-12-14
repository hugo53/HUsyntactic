'''
Created on 09-12-2011

@author: hoangnm
'''

__author__  = "Minh-Hoang, Nguyen <hoangnm.53@gmail.com>"
__date__    = "$December 09, 2011$"
__version__ = "1.0"

import argparse
import time
from   hu.utils.uIO import IO
from   hu.cky.ckyAlgorithm import CKY

if __name__ == '__main__':
    # For help function
    usage = "usage: %(prog)s [options] \npython HUsyntactic -h " \
                                                                    "for help"
    
    
    parser = argparse.ArgumentParser(prog="HUsyntactic", usage=usage,
            version="HUsyntactic "+__version__,
            description='A syntactic analyzer uses CYK algorithm.',
            epilog="(C) 2011 by Minh-Hoang, Nguyen")
    parser.add_argument("-g", "--grammar", dest="grammar",required=True,
                        help="name of the file with the CNF grammar")
    parser.add_argument("-l","--lexicon", dest="lexicon",required=True,
                        help="name of the file with the lexicon")
    parser.add_argument("-s","--sentence", dest="sentence",required=True,
                        help="list of input sentences separate" \
                                                     "by newline symbol")
    parser.add_argument("-o","--outfile", dest="outfile", required=True, 
                        help="path of outfile")
    parser.add_argument("-q", "--quiet",
            action="store_false", dest="DEBUG", default=True,
            help="don't print the chart content  [default True]")
    args = parser.parse_args()
    
    #call parser
    # Theory of call:
    #        - args.dest : contains content user entered
    #        - e.g: args.grammar will return file name of file contain grammar
    if args:
        try:
            #Call to main parser
            #Read file
            io = IO(args.grammar, args.lexicon, args.sentence)
            listGrammar  = io.readGrammar()
            listLexicon  = io.readLexicon()
            listSentence = io.readSentence()
            #Run CYK
            cykInstance = CKY(listGrammar, listLexicon, args.outfile)
            startTime = time.clock()
            for sent in listSentence:
                cykInstance.syntacticAnalyzer(sent)  
            stopTime = time.clock()
            print "Analysis success. Please check output file! \nTime is: ",stopTime-startTime                
        except IOError:
            print "Cannot open files. Please check your files!"