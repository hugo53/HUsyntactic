'''
Created on 10-12-2011

@author: hoangnm
'''
from cky.datastructure.dsGrammar import Grammar
from cky.datastructure.dsLexicon import Lexicon

class CKYIO:
    '''
    IO operators:
        * read grammar file
        * read lexicon file
        * read sentence file
    '''
     
    def __init__(self, grammarFile, lexiconFile, sentenceFile):
        '''
        Constructor with 3 parameters:
            * grammar file
            * lexicon file
            * sentence file
        '''
        self.grammarFile = grammarFile
        self.lexiconFile = lexiconFile
        self.sentenceFile= sentenceFile 
        self.listOfGrammars=[]
        self.listOfLexicons=[] 
        self.listOfSentences=[]      
        
    def readGrammar(self):
        '''
        Read grammar file
        
        Parameters
        ----------
        
        Returns
        -------
        out: a list contains Grammar objects
        '''
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
        '''
        Read lexicon file
        
        Parameters
        ----------
        
        Returns
        -------
        out: a list contains Lexicon objects
        '''
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
        '''
        Read sentence file
        
        Parameters
        ----------
        
        Returns
        -------
        out: a list contains sentence strings
        '''
        infile = open(self.sentenceFile, 'r')
        for line in infile.readlines():
            if line.startswith('#'):
                continue
            self.listOfSentences.append(line)
        infile.close()
        return self.listOfSentences
    
    def getListOfGrammars(self):
        '''
        Get list of grammar
        
        Parameters
        ----------
        
        Returns
        -------
        out: a list of Grammar objects
        '''
        return self.listOfGrammars
    
    def getListOfLexicons(self):
        '''
        Get list of lexicon
        
        Parameters
        ----------
        
        Returns
        -------
        out: a list of Lexicon objects
        '''
        return self.listOfLexicons
    
    def getListOfSentences(self):
        '''
        Get list of sentence
        
        Parameters
        ----------
        
        Returns
        -------
        out: a list of sentence
        '''
        return self.listOfSentences