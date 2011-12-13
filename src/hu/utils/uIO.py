'''
Created on 10-12-2011

@author: hoangnm
'''
from hu.datastructure.dsGrammar import Grammar
from hu.datastructure.dsLexicon import Lexicon

class IO:
    '''
    IO operator
    '''
     
    def __init__(self, grammarFile, lexiconFile, sentenceFile):
        '''
        Constructor
        '''
        self.grammarFile = grammarFile
        self.lexiconFile = lexiconFile
        self.sentenceFile= sentenceFile 
        self.listOfGrammars=[]
        self.listOfLexicons=[] 
        self.listOfSentences=[]      
        
    def readGrammar(self):
        infile = open(self.grammarFile,'r')
        for line in infile.readlines():
            if line.startswith('#'):
                continue
            listWords = line.split()
            if len(listWords)==4:
                left = listWords[0]
                rightFirst = listWords[2]
                rightSecond = listWords[3]
                grammar = Grammar(left, rightFirst, rightSecond)
                self.listOfGrammars.append(grammar)
            else:
                print "Error at Grammar form (length less than 4)"
        infile.close()
        return self.listOfGrammars
    
    def readLexicon(self):
        infile = open(self.lexiconFile, 'r')
        for line in infile.readlines():
            if line.startswith('#'):
                continue
            listWords = line.split()
            if len(listWords)==3:
                left = listWords[0]
                right = listWords[2]
                lexicon = Lexicon(left, right)
                self.listOfLexicons.append(lexicon)
            else:
                print "Error at Lexicon form (length less than 4"
        infile.close()
        return self.listOfLexicons
    
    def readSentence(self):
        infile = open(self.sentenceFile, 'r')
        for line in infile.readlines():
            if line.startswith('#'):
                continue
            self.listOfSentences.append(line)
        infile.close()
        return self.listOfSentences
    
    
    #Get funcs
    def getListOfGrammars(self):
        return self.listOfGrammars
    def getListOfLexicons(self):
        return self.listOfLexicons
    def getListOfSentences(self):
        return self.listOfSentences
    

    