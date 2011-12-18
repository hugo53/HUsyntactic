'''
Created on 17-12-2011

@author: hoangnm
'''
from earley.datastructure.dsRule import Rule
class IO:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    #Use for grammar file and lexicon file
    #Return a list of rule
    def readGrammar(self,grammarFile):
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
        listOfSentences = []
        infile = open(sentenceFile, 'r')
        for line in infile.readlines():
            if line.startswith('#'):
                continue
            listOfSentences.append(line)
        infile.close()
        return listOfSentences