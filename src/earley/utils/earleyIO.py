'''
Created on 17-12-2011

@author: hoangnm
'''

from earley.datastructure.dsRule import Rule

class EarleyIO:
    '''
    classdocs
    '''
################################################################################
#BEGIN CONSTRUCTOR
    def __init__(self):
        '''
        A empty constructor
        In this class, call all functions with one argument: file name 
        '''
#END CONSTRUCTOR
################################################################################

################################################################################
# BEGIN READ FILE FUNCTIONS
# Note  : a string start with '#' is a comment, thus it is ignored
 
    def readGrammar(self,grammarFile):
        '''
        Read grammar file to parse to Rule objects 
        
        Parameters
        ----------
        grammarFile: file name of file contains grammar strings
        
        Returns
        -------
        out: a list contains rules is generated by grammar strings           
        '''
        listGrammar = []
        infile = open(grammarFile,'r')
        for line in infile.readlines():
            if line.startswith('#'):
                continue
            listWords = line.split()
            left = listWords[0]
            rightTwo = []
            for i in range(2, len(listWords)):
                rightTwo.append(listWords[i])
                    
            rule = Rule(left, [], rightTwo)
            listGrammar.append(rule)
            
        infile.close()
        return listGrammar

    def readLexicon(self,lexiconFile):
        '''
        Read lexicon file to parse to Rule objects 
        
        Parameters
        ----------
        lexiconFile: file name of file contains lexicon strings
        
        Returns
        -------
        out: a list contains rules is generated by lexicon strings           
        '''
        listLexicon = []
        infile = open(lexiconFile,'r')
        for line in infile.readlines():
            if line.startswith('#'):
                continue
            listWords = line.split()
            left = listWords[0]
            rightTwo = []
            for i in range(2, len(listWords)):
                rightTwo.append(listWords[i])
                    
            rule = Rule(left, [], rightTwo, True)
            listLexicon.append(rule)
            
        infile.close()
        return listLexicon

    def readSentence(self, sentenceFile):
        '''
        Read sentence file  
        
        Parameters
        ----------
        sentenceFile: file name of file contains sentence strings
        
        Returns
        -------
        out: a list of string           
        '''
        listOfSentences = []
        infile = open(sentenceFile, 'r')
        for line in infile.readlines():
            if line.startswith('#'):
                continue
            listOfSentences.append(line)
        infile.close()
        return listOfSentences

#END READ FILE FUNCTIONS
################################################################################